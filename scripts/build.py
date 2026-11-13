"""Build a deployment-ready static directory using only Python's standard library."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parent.parent
out = root / 'dist'
out.mkdir(exist_ok=True)
shutil.copy2(root / 'index.html', out / 'index.html')
for name in ('assets', 'demos'):
    shutil.copytree(root / name, out / name, dirs_exist_ok=True)
print(f'Built static site: {out}')
