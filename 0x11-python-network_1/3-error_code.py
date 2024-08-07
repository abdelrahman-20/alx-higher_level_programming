#!/usr/bin/python3
"""Handling HTTP Error"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
