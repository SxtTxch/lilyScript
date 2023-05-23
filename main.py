from sys import *
from interpreter import *
import os

if __name__ == '__main__':
    ran = False
    for element in os.listdir():
        if element == "index.lilyS":
            ran = True
            parse("index.lilyS")
            break
    if not ran:
        parse(argv[1])
        