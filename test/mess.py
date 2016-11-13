import sys

file = open('mess.txt', 'r')
outfile = open('code.txt', 'w')

while 1:
    char = file.read(1)
    if char == '#' or char == '&' or char == '@' or char == '$' or char == '!' or char == '*' or char == '^' or char == '{' or char == '}' or char == '_' or char == '(' or char == ')' or char == '+' or char == '[' or char == ']' or char == '%':
        char = '_'
        outfile.write(char)
    if not char: break
    print char

file.close()
outfile.close()

sys.exit
