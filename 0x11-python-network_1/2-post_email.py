#!/usr/bin/python3
"""POST An Email To URL"""

if __name__ == "__main__":
    import sys
    import urllib.parse as parse
    import urllib.request as request

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email})
    data = data.encode("ascii")

    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
