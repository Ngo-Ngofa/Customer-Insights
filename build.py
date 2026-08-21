"""Inline the generated data into the template to produce index.html."""
from pathlib import Path

root = Path(__file__).parent
template = (root / "pipeline" / "template.html").read_text()
data = (root / "data" / "aggregates.json").read_text()
out = template.replace("/*__DATA__*/", data)
(root / "index.html").write_text(out)
print(f"index.html written, {len(out)//1024} KB")
