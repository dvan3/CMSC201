#Filename:    hw3.py
#Written by:  Dave Van
#Date:        2/23/10
#Section #:   06
#Email:       dvan3@umbc.edu
#Description: This program has python code that will
#decode a message that was encoded with a Caesar cipher.
#Using letter frequencies to determine the rotation length.

def main():

    import string
    
    #Constants
    ALPHA = 26
    ROTATION = 21
    
    #Explaination of what this program does
    print "This program will decode a message that was encoded with a Caesar"
    print "cipher by using letter frequencies to determine the rotation.\n"

    #Get a string from the user
    str = raw_input("")

    #Goes through every character in the string
    for char in str:

        #Checks if each character is a letter
        if char.isalpha():

            #counts how many times each letter is used
            count = string.count(str, char)
            print count,

            #Gets the ASCII values
            ascii = ord(char)
            
            #Checks if the ASCII values are between 65 and 91.
            if ascii in range(65, 91):
                ascii += ROTATION

                #Keeps the letters from going past Z into other ASCII values
                if ascii > ord('Z'):
                    ascii -= ALPHA
                    
            preamble = chr(ascii)
            #Print the results
            print preamble,

main()
            
