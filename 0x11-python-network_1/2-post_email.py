#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
 And displays the body of the response
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urib.request.Request(url, data)
    with urllib.requlencode(value).encode("ascii")

    request = urllest.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
