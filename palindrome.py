#!/usr/bin/env python3
def is_palindrome(x):
        if x.lower() == ''.join(reversed(x)).lower():
            is_palindrome.check = True
        else:
            is_palindrome.check = False
