#! /usr/bin/env python3

import requests, sys, webbrowser

print("Searching...")

query = " ".join(sys.argv[1:])
url = f"https://pypi.org/search/?q={query}"

# Use pypi.org search results via JSON API (through a hidden endpoint)
headers = {"Accept": "application/vnd.pypi.simple.v1+json", "User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# Fallback to HTML open, since official JSON API isn't available for search
# We'll just open the actual PyPI search page in a browser as a backup
print("Opening search page in browser...")
webbrowser.open(url)
