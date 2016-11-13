# filename:   lab12.py
# Written by: Dave Van
# Date:       5/3/10

import sys
import string

NUM_ARGS = 2

# getListOfStrings() opens a file, reads each line of the file, strips
# any leading or trailing whitespace, creates a list of the strings,
# closes the file and returns the list of strings
#
# Input:  the name of the file to open
# Output: the list of strings read from the file
def getListOfStrings(filename):

    origList = []
    infile = open(filename, 'r')
    
    for line in infile:
        str = string.strip(line)
        origList.append(str)

    infile.close()
    return origList

# purgeString() takes a string and makes a new string which has been
# purged of all the non-alphabetic characters.  The purged string is
# in all capitals
#
# Input:  a string
# Output: an all-caps string of letters that were in the string passed in
def purgeString (str):

    purged = ''
    
    str = string.upper(str)

    for ch in str:
        if(ch >= 'A' and ch <= 'Z'):
	    purged = purged + ch
    
    return purged

# isPalindrome() determines whether the string passed in is a palindrome.
# This is a recursive function.
#
# Inputs: str, the all-caps, purged string
#         left, the left index
#         right, the right index
# Output: True or False
def isPalindrome (str, left, right):

    if (right - left) <= 0:
        return True
    else:
        return (isPalindrome(str, left + 1, right - 1) and
                str[left] == str[right])

def main():

    # find number of command-line arguments
    lengthArgs = len(sys.argv)

    # if the number is not correct print instructions
    # for running the program and exit
    if  lengthArgs < NUM_ARGS:
        print "This program requres commandline arguments."
        print "The first argument is the executable file: lab12.py"
        print "The second argument is the file being read: strings.dat"
        sys.exit()
    


    # call getListOfStrings to get the origList
    origList = getListOfStrings(sys.argv[1])

    print "The palindromes in the file are:"

    # for each of the strings in origList
    for line in origList:

        # make a tempStr by calling purgeString()
        # tempStr will be in all uppercase with non-letters removed
        tempStr = purgeString(line)

        # determine if tempStr is a palindrome by calling isPalindrome()
        if isPalindrome(tempStr, 0, len(tempStr) - 1):
            # if it is, print the original string tempStr was made from
            print line


main()

