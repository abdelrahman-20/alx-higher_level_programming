#!/usr/bin/python3
"""A script that sends a POST request"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.post(url, {"email": email})
    print(res.text)
