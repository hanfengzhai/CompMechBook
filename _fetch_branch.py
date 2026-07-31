#!/usr/bin/env python3
"""Fetch all files from cursor/computational-mechanics-book-2865 into workspace."""
import json
import os
import urllib.request

REF = "966f62db6554a310c08303fa3c4ef4fd835aa7a7"
REPO = "hanfengzhai/CompMechBook"
ROOT = os.path.dirname(os.path.abspath(__file__))


def api(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def fetch_tree(sha, prefix=""):
    data = api(f"https://api.github.com/repos/{REPO}/git/trees/{sha}?recursive=1")
    for item in data["tree"]:
        if item["type"] != "blob":
            continue
        path = item["path"]
        if prefix:
            path = f"{prefix}/{path}" if not path.startswith(prefix) else path
        yield path


def download_file(path):
    url = f"https://raw.githubusercontent.com/{REPO}/{REF}/{path}"
    with urllib.request.urlopen(url) as r:
        return r.read()


def main():
    root_tree = api(f"https://api.github.com/repos/{REPO}/git/commits/{REF}")["tree"]["sha"]
    paths = list(fetch_tree(root_tree))
    print(f"Fetching {len(paths)} files from {REF[:8]}...")
    for path in paths:
        dest = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        content = download_file(path)
        with open(dest, "wb") as f:
            f.write(content)
        print(f"  {path}")
    print("Done.")


if __name__ == "__main__":
    main()
