import math
import os
import sys

import requests

print (sys.version)
print(sys.executable)


def greet(who_to_greet):    
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("http://www.parduodu.com")
print(r.status_code)

