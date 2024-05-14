# Challenge: Write a python function to determine if a given string is a palindrome.
# Input: string to evaluate
# Output: Boolean value
# only consider letters A-Z & ignore case

import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower())) #converts all letters to lowercase
    backwards = forwards[::-1] # stride through the string from the last to first
    return forwards == backwards # compare the strings forwards and backwards and return if they're equal