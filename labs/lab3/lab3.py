#Name: Dave Van
#Caesar Cipher

import string

RAW_AMOUNT = 13
ALPHABET_LENGTH = 26

user_string = raw_input("Please enter a string: ")

uppers = string.upper(user_string)
#string.strip(user_string)

for char in uppers:
    if char != ' ':
        asciival = ord(char)
        asciival += RAW_AMOUNT

        if asciival > ord('Z'):
            asciival -= ALPHABET_LENGTH

    print chr(asciival),
        
    
    
    
    
