#! /usr/bin/env python3
# strongPasswordDetection.py - A function that uses regular expressions to make sure the password string
# that is passed is strong.

import re

characterCheck = re.compile(r'\d+')
upperCheck = re.compile(r'[A-Z]+')
lowerCheck = re.compile('[a-z]+')

def passwordCheck(text):
    if characterCheck.search(text) and upperCheck.search(text) and lowerCheck.search(text):
        return True
    else:
        return False

print('Enter your password:\n(must be at least eight characters long,\ncontain both uppercase and lowercase characters,\nand has at least one digit)')
text = input()
# print(passwordCheck(text))            # removed for more flexible messages

checkRun = passwordCheck(text)
if checkRun == True:
    print(text + ' is a sufficient password.')
else:
    print(text + ' does not meet minimum password requirements.')
