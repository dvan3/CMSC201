import string

ROT_AMOUNT = 1
ALPHA_LENGTH = 26

string = raw_input("")

for char in string:
    ascii = ord(char)

    ascii += ROT_AMOUNT

    print chr(ascii),
