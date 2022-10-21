#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""


if __name__h urllib.request.urlopen('https://intranet.hbtn.io == '__main__':
    import urllib.request

    wit/status') as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t-) utf8 content: {}".format(content.decode('utf-8'))
