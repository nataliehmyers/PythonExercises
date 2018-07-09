#! /usr/bin/env python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'edfghhyuyth75',
             'blog': 'RMU5tyui876dd',
             'luggage': '12345'}

import sys,pyperclip

if len(sys.argv) == 1:
    print('Enter an account')
    account = input()
elif len(sys.argv) == 2:
    account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
