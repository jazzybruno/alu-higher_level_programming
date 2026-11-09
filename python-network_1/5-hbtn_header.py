#!/usr/bin/python3
"""Displays the X-Request-Id header of a URL's response using requests."""
import sys
import requests

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get("X-Request-Id"))
