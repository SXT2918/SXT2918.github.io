from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for attribute in ("src", "href", "poster"):
            value = values.get(attribute)
            if value:
                self.paths.append(value)


root = Path(__file__).resolve().parent.parent
parser = AssetParser()
parser.feed((root / "index.html").read_text(encoding="utf-8"))

missing = []
for raw in parser.paths:
    parsed = urlparse(raw)
    if parsed.scheme or raw.startswith(("#", "mailto:")):
        continue
    path = root / parsed.path
    if not path.exists():
        missing.append(parsed.path)

if missing:
    raise SystemExit("Missing local assets:\n" + "\n".join(sorted(set(missing))))

print("All referenced local assets exist.")
