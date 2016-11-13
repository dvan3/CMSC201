#File name: lab4.py
#Name:      Dave Van

import sys

def main():
    num = input("Enter a positive integer: ")
    if type(num) != int or num <= 0:
        print "You fool! I asked for a positive integer!"
        sys.exit()

    count = 0

    for i in range(1,num):
        if num % i == 0:
            count += i

    if count == num:
        print "This number is perfect."
    else:
        print "This number is imperfect"

main()
        
