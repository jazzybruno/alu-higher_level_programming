#!/usr/bin/python3
"""Adds all command-line arguments to a list saved in add_item.json."""
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    items = load_from_json_file(filename) if os.path.exists(filename) else []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
