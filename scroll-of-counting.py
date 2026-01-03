#!/usr/bin/env python3
import os
import json
import datetime

# --- 1. Ranger: Top-Level Awareness ---
# This script finds its own location (the root of your repo)
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_ROOT, "shadow-book.json")

def scan_codex():
    total_words = 0
    file_stats = []
    
    for root, dirs, files in os.walk(REPO_ROOT):
        # Druid: Ignore the .git folder and the script itself
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith(('.txt', '.md')) and file != "shadow-book.json":
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        count = len(f.read().split())
                        total_words += count
                        # Monk: Track specific file growth
                        file_stats.append({"name": file, "words": count})
                except:
                    pass
    return total_words, file_stats

# --- 2. Druid: Log the State ---
words, stats = scan_codex()
now = datetime.datetime.now().isoformat()

entry = {
    "timestamp": now,
    "total_words": words,
    "daily_drift": words, # Future: calculate difference from last entry
    "note": "A record of the scrawl before the moon set."
}

# Persistent Logic: Save within the repo so it can be pushed to Codeberg
history = []
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        history = json.load(f)

history.append(entry)

with open(LOG_FILE, 'w') as f:
    json.dump(history, f, indent=2)

print(f"Monk: {words} words recorded in the Codex ledger.")