#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    commits = requests.get(url, params={"per_page": 10}).json()
    for commit in commits[:10]:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")))
