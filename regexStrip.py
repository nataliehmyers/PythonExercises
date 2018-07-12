#! /usr/bin/env python3
# regexStrip.py - A function that takes a string and does the same thing as the strip() string method.

import re

def regexStrip(string, x):
    regex = '([' + x + ']*)(.*)([' + x + ']*$)'
    strip = re.compile(regex)
    print(strip.search(string).group(2))
