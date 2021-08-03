# Vulture feeds on Dead Code!

import os
import numpy as np
import pandas as pd

class Greeter:
    def greet(self):
        print("Hi")

def hello_world():
    var = 123
    var2 = 1234 + 56
    var3 = 10
    message = "Hello World!"
    greeter = Greeter()
    greet_func = getattr(greeter, "greet")
    greet_func()

if __name__ == "__main__":
    hello_world()