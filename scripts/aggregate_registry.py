import yaml, glob, os

    entries = []
    for meta in glob.glob("inventory/snippets/*/metadata.yaml"):
        with open(meta) as f:
            data = yaml.safe_load(f)
        slug = os.path.basename(os.path.dirname(meta))
        data.setdefault("path", f"snippets/{slug}")
        entries.append(data)

    with open("registry.yaml", "w") as f:
        yaml.safe_dump({"snippets": entries}, f)

    lines = ["| Slug | Version | Status | Description |",
             "|------|---------|--------|-------------|"]
    for e in entries:
        desc = e.get("description", "—")
        lines.append(f"| {e['name']} | {e['version']} | {e['status']} | {desc} |")

    with open("registry.md", "r") as f:
        content = f.read()

    start = content.index("<!-- SNIPPET_TABLE_START -->") + len("<!-- SNIPPET_TABLE_START -->")
    end = content.index("<!-- SNIPPET_TABLE_END -->")
    updated = content[:start] + "
" + "
".join(lines) + "
" + content[end:]

    with open("registry.md", "w") as f:
        f.write(updated)
