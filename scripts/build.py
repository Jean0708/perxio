"""Validate the prototype and prepare the public GitHub Pages artifact."""
from html.parser import HTMLParser
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent


class PageCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                raise ValueError(f"Duplicate HTML id: {element_id}")
            self.ids.add(element_id)


source = ROOT / "index.html"
html = source.read_text(encoding="utf-8")
if "<title>" not in html or "</html>" not in html:
    raise ValueError("index.html is not a complete page")
PageCheck().feed(html)
output = ROOT / "_site"
output.mkdir(exist_ok=True)
shutil.copy2(source, output / "index.html")
(output / ".nojekyll").touch()
pages = ROOT / "docs"
pages.mkdir(exist_ok=True)
shutil.copy2(source, pages / "index.html")
(pages / ".nojekyll").touch()
print(f"Prepared {output / 'index.html'}")
print(f"Prepared {pages / 'index.html'} for GitHub Pages")
