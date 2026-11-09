#!/usr/bin/python3
"""Fetches the intranet status URL with requests and shows the body."""
import requests

if __name__ == "__main__":
    body = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
