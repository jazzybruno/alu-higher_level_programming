#!/usr/bin/python3
"""Searches users by letter on http://0.0.0.0:5000/search_user."""
import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        user = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if user:
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")
