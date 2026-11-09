#!/usr/bin/python3
"""POSTs an email to a URL with urllib and displays the decoded body."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
