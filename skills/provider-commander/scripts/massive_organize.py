#!/usr/bin/env python3
"""Trabajo masivo de organizacion: inventaria repos locales, los clasifica en paralelo
con modelos gratis, y sintetiza un plan maestro con DeepSeek Pro (maximo razonamiento).
Escribe reports/ORGANIZACION-MAESTRA.md
"""
import json, os, subprocess, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent))
import orchestrator as O  # noqa: E402

ROOTS = [Path.home(), Path.home() / "belentani-repos-master", Path.home() / "Documents", Path.home() / "Desktop", Path.home() / "repos"]
SKIP = {"node_modules", "AppData", ".git", "dist", "build", ".next"}
REPORT = Path(__file__).parent.parent / "reports" / "ORGANIZACION-MAESTRA.md"

def git_remote(p):
    try:
        out = subprocess.run(["git", "-C", str(p), "remote", "get-url", "origin"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip()
    except Exception:
        return ""

def discover():
    repos = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.iterdir()):
            if not p.is_dir() or p.name.startswith(".") or p.name in SKIP:
                continue
            if not (p / ".git").exists():
                continue
            try:
                files = sum(1 for f in p.rglob("*") if f.is_file())
            except Exception:
                files = 0
            repos[str(p)] = {"name": p.name, "path": str(p), "files": files, "remote": git_remote(p)}
    return list(repos.values())

def classify_batch(batch, idx):
    listing = "\n".join(f"- {r['name']} | {r['files']} archivos | {r['remote'] or 'sin remote'}" for r in batch)
    prompt = ("Clasifica cada repositorio y recomienda accion. Categorias: educacion, musica, web, ia, infra, "
              "seguridad, archivo, experimento. Acciones: mantener, archivar, fusionar, borrar, revisar. "
              "Devuelve SOLO un JSON array con objetos {name, category, action, reason}. "
              "Repositorios:\n" + listing)
    r = O.call_with_fallback(O.REG["routing"]["classify"], prompt, max_tokens=2500)
    return {"batch": idx, "ok": r.get("ok"), "provider": r.get("provider"), "model": r.get("model"),
            "text": r.get("text", ""), "error": r.get("error")}

def main():
    repos = discover()
    print(f"repos encontrados: {len(repos)}")
    if not repos:
        return 2
    B = 12
    batches = [repos[i:i + B] for i in range(0, len(repos), B)]
    print(f"lotes: {len(batches)} (de {B})")

    results = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = [ex.submit(classify_batch, b, i) for i, b in enumerate(batches)]
        for f in as_completed(futs):
            r = f.result(); results.append(r)
            print(f"  lote {r['batch']:2} {'OK' if r['ok'] else 'XX'} {(r.get('provider') or '-')}/{r.get('model') or '-'}")

    # sintesis con razonamiento maximo (DeepSeek Pro, dentro del limite 25/h)
    print("sintesis con deepseek-v4-pro...")
    joined = "\n\n".join(f"--- lote {r['batch']} ---\n{r['text']}" for r in results)
    synth_prompt = (
        "Eres arquitecto de informacion. Tienes clasificaciones de repos locales de un desarrollador. "
        "Produce un PLAN MAESTRO DE ORGANIZACION en markdown con: "
        "1) taxonomia de carpetas propuesta (raiz y subcarpetas), "
        "2) tabla repo -> categoria -> accion, "
        "3) duplicados/solapamientos detectados, "
        "4) top 10 acciones prioritarias, "
        "5) criterio de parada. "
        "Se conciso, accionable, sin relleno. Datos:\n\n" + joined[:24000])
    r = O.call_with_fallback(O.REG["routing"]["synth"], synth_prompt, max_tokens=8000)
    print(f"sintesis: {'OK' if r.get('ok') else 'XX'} {r.get('provider')}/{r.get('model')} {r.get('error') or ''}")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    md = ["# Organizacion maestra del workspace", "",
          f"- repos: {len(repos)}  lotes: {len(batches)}",
          f"- sintesis: {r.get('provider')}/{r.get('model')}  ok={r.get('ok')}", "",
          "## Inventario", ""]
    for x in sorted(repos, key=lambda z: z["name"].lower()):
        md.append(f"- `{x['name']}` ({x['files']} archivos) {x['remote']}")
    md += ["", "## Plan maestro (sintesis)", "", r.get("text", r.get("error", "")), "",
           "## Clasificaciones por lote", ""]
    for x in sorted(results, key=lambda z: z["batch"]):
        md += [f"### lote {x['batch']} ({x.get('provider')}/{x.get('model')})", "", x.get("text", x.get("error", "")), ""]
    REPORT.write_text("\n".join(md), encoding="utf-8")
    print(f"\ninforme: {REPORT}")
    cost = sum(u["cost_usd"] for u in O._usage.values())
    print(f"coste estimado: ${cost:.4f}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
