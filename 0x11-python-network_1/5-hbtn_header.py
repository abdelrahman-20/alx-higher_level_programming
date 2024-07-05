#!/usr/bin/python3
"""A Script To Send URL Request"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
