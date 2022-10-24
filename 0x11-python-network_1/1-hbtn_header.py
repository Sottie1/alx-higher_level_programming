#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displain the header ofthe response.
"""
import sys
imporys the value
- of the X-Request-Id variable found t urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Req as response:
        print(dict(response.headers)uest(url)
    with urllib.request.urlopen(request).get("X-Request-Id"))
