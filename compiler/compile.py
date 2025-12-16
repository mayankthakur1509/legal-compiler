import os, yaml
from slugify import slugify

BASE_OUT = "dist"

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

def page(title, body):
    return f"""<!doctype html>
<html>
<head>
<title>{title}</title>
<meta charset='utf-8'>
</head>
<body>
<h1>{title}</h1>
{body}
</body>
</html>"""

def run():
    lawyers = load_yaml("firm-example/lawyers.yaml")
    practices = load_yaml("firm-example/practice_areas.yaml")

    for lw in lawyers:
        slug = slugify(lw["name"])
        root = f"{BASE_OUT}/lawyers/{slug}"

        write(f"{root}/index.html",
              page(lw["name"], f"<p>{lw['role']}</p>"))

        for persona in ["cfo", "cpa", "client"]:
            write(f"{root}/persona-{persona}.html",
                  page(f"{lw['name']} – {persona.upper()}",
                       f"<p>Persona page for {persona}</p>"))

        write(f"{root}/formfree.html",
              page("Free Download", "<a href='#'>Download Guide</a>"))

        for p in lw["practice_areas"]:
            pslug = slugify(p)
            write(f"{root}/practice-area/{pslug}/index.html",
                  page(p, f"<p>{lw['name']} – {p}</p>"))

    for p in practices:
        pslug = slugify(p)
        write(f"{BASE_OUT}/practice-areas/{pslug}/index.html",
              page(p, f"<p>{p} overview</p>"))

    os.makedirs(f"{BASE_OUT}/semantic", exist_ok=True)
    with open(f"{BASE_OUT}/semantic/schema.json", "w") as f:
        f.write("{}")

    print("✓ Multi-lawyer site generated")

if __name__ == "__main__":
    run()
