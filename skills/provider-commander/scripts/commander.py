#!/usr/bin/env python3
"""provider-commander: reparte tareas entre proveedores y las ejecuta EN PARALELO.
Gratis primero. Rotacion de llaves. Sin secretos en disco.

Modos:
  split    (default) cada tarea va al proveedor mas barato capaz
  compare  el mismo prompt va a N proveedores para comparar respuestas

Uso:
  python commander.py --mode split --tasks tasks.json
  python commander.py --mode compare --prompt "explica X" --providers groq,zai,morph
  python commander.py --mode split --tasks '[{"id":"t1","prompt":"..."}]'
"""
import argparse, json, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import providers as P  # noqa: E402

KIND_PATTERNS = [
    ("judge",    r"\b(audita|auditoria|security|seguridad|vulnerabilidad|pentest|revisa critico)\b"),
    ("reason",   r"\b(arquitectura|architecture|disena|planifica|razona|reason|analiza a fondo|estrategia|demuestra)\b"),
    ("edit",     r"\b(edita|edit|patch|aplica|apply|diff|multi-archivo|refactor)\b"),
    ("classify", r"\b(clasifica|etiqueta|extrae|json|tabla|lista|resumen)\b"),
    ("trivial",  r"\b(renombra|rename|formatea|formato|traduce|traducir|hola|ping)\b"),
]

def infer_kind(prompt: str) -> str:
    t = prompt.lower()
    for kind, rx in KIND_PATTERNS:
        if re.search(rx, t):
            return kind
    return "code"

def run_task(task: dict) -> dict:
    kind = task.get("kind") or infer_kind(task["prompt"])
    if task.get("provider") and task.get("model"):
        provider, model = task["provider"], task["model"]
    else:
        provider, model = P.ASSIGN.get(kind, ("groq", "openai/gpt-oss-120b"))
    t0 = time.time()
    out = P.chat(provider, model, task["prompt"], max_tokens=task.get("max_tokens", 2048),
                 system=task.get("system"))
    out.update({"id": task.get("id", task["prompt"][:24]), "kind": kind,
                "elapsed_s": round(time.time() - t0, 1)})
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="split", choices=["split", "compare"])
    ap.add_argument("--tasks", help="JSON: lista de tareas o ruta a fichero")
    ap.add_argument("--prompt", help="prompt unico (modo compare)")
    ap.add_argument("--providers", default="groq,zai,morph", help="compare: lista separada por comas")
    ap.add_argument("--max-workers", type=int, default=6)
    ap.add_argument("--out", default=str(Path(__file__).parent.parent / "references" / "last_run.json"))
    args = ap.parse_args()

    if args.mode == "compare":
        if not args.prompt:
            print("compare requiere --prompt"); return 2
        tasks = []
        for prov in args.providers.split(","):
            prov = prov.strip()
            model = P.ASSIGN.get("code", (prov, "openai/gpt-oss-120b"))[1]
            if prov == "openrouter": model = "openrouter/auto"
            elif prov == "zai": model = "glm-4.5-flash"
            elif prov == "morph": model = "morph-dsv41flash"
            tasks.append({"id": prov, "prompt": args.prompt, "provider": prov, "model": model})
    else:
        raw = args.tasks
        if raw and Path(raw).exists():
            raw = Path(raw).read_text(encoding="utf-8")
        tasks = json.loads(raw) if raw else []
        tasks = [{"prompt": t} if isinstance(t, str) else t for t in tasks]

    if not tasks:
        print("sin tareas"); return 2

    print(f"commander: {len(tasks)} tarea(s), modo={args.mode}, paralelo={args.max_workers}")
    results = []
    with ThreadPoolExecutor(max_workers=args.max_workers) as ex:
        futs = {ex.submit(run_task, t): t for t in tasks}
        for f in as_completed(futs):
            r = f.result()
            results.append(r)
            mark = "OK " if r.get("ok") else "XX "
            head = (r.get("text") or r.get("error") or "")[:110].replace("\n", " ")
            print(f"{mark}[{r['id']:16}] {r['provider']}/{r['model']:28} {r['elapsed_s']:5}s  {head}")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    ok = sum(1 for r in results if r.get("ok"))
    print(f"\n{ok}/{len(results)} OK  ->  {args.out}")
    return 0 if ok == len(results) else 1

if __name__ == "__main__":
    sys.exit(main())
