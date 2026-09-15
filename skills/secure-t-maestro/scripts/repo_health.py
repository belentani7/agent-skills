#!/usr/bin/env python3
"""Print a compact, deterministic health report for secure-t repositories."""
from pathlib import Path
import json
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
print(f"root={root}")
for rel in ["README.md", "package.json", "client", "server", "ai", "academic", "labs", "audit", "tests", "docs/SECURITY.md"]:
    p = root / rel
    print(f"exists[{rel}]={p.exists()}")

pkg = root / "package.json"
if pkg.exists():
    try:
        data = json.loads(pkg.read_text())
        print(f"package.name={data.get('name')}")
        print("scripts=" + ",".join(sorted(data.get("scripts", {}))))
    except Exception as exc:
        print(f"package.error={type(exc).__name__}")

java = sorted(str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and (p.suffix == ".java" or p.name in {"pom.xml", "build.gradle", "build.gradle.kts"}))
print("java.files=" + (",".join(java) if java else "none"))
