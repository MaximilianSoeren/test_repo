import sys
from os import rename

import requests

# print sys.version
# print sys.executable


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


r = requests.get("https://msoerenpollak.com")
print(r.status_code)
