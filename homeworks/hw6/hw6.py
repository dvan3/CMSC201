#Filename:    hw6.py
#Written by:  Dave Van
#Date:        3/22/10
#Seciton:     06
#Email:       dvan3@umbc.edu
#Description:
#Using the hailstone sequence, the user will enter a number and if the number
#is even divide it in half, if the number is odd, multiply it by three and add
#one to it. It will also use a menu. The user will choose what they want to see
#They can choose to see an individual value, range of values, or to find the
#longest chain. To quit the program they will use 'Q' or 'q'

#Constants
MIN = 1
MAX = 10000
QUES = "Please enter an integer"
START_QUES = "Enter a starting integer"
END_QUES = "Enter an ending integer"

#printGreeting prints the greeting that explains what this program does
#Input: None
#Output: The greeting
def printGreeting():
    print "\nThis program uses the hailstone sequence. The user will enter a"
    print "number, if it is even then divide it in half. If it is odd, then"
    print "multiply the number by three and add one.\n"

#printMenu() prints the menu for the user
#Inputs: none
#Outputs: The menu
def printMenu():
    print "\tI - view sequence for an Indiviual value"
    print "\n\tR - view sequence for a Range of vales"
    print "\n\tL - Find the Longest chain"
    print "\n\tQ - Quit\n"

#getValidInt() will compose a question for the user and if the user enters an
#integer out of the range, it will keep repeating the question until it is
#statisfied
#Input:  the question, question; the starting value, min; the ending value, max
#Output: the composed question asking the user for an intger for the starting
#value and the ending value
def getValidInt(question, min, max):

    #use a bad value to enter the loop
    value = max + 1

    #compose the prompt
    prompt = question + " (" + str(min) + "-" + str(max) + "): "

    #continue to get values until the user enters a valid one
    while value == "" or value < min or value > max:
        value = raw_input(prompt)
        if len(value) != 0:
            value = int(value)

    #return a valid value
    return value

#hailstone() takes a number and prints the hailstone sequence
#Input:  an integer, n
#Output: the hailstone sequence and the length of the sequence
def hailstone(n):

    #makes a list from n
    hail_sequence = [n]
    print n,

    #a sentinal while loop, while n is larger than one, keep going.
    while n > 1:

        #if even, append n to the list hail_sequence, then print n
        if isOdd(n) == False:
            hail_sequence.append(n)
            n = n / 2
            print " ->", n,

        #if odd, append n to the list hail_sequence, then print n
        elif isOdd(n) == True:
            hail_sequence.append(n)
            n = 3 * n + 1
            print " ->", n,

    #gets the length of the list from hail_sequence, then prints length
    length = len(hail_sequence)
    print "; length = ", length
    print

    #returns length
    return length

#longestChain() finds the longest chain from a range the user inputs
#Input:  a starting value, start; an ending value, end
#Output: prints out the chain with the longest length, and then the length
def longestChain(start, end):
    longestLength = 1
    length = 0
    
    #for loop that finds the length of the longest chain 
    for i in range(start, end + 1):
        if length <= hailstone(i):
            longestLength = i
            length = hailstone(i)
            
    #prints the longest chain
    print longestLength, " had the longest chain ", length
    print
    

#isOdd() takes a positive integer as an argument and returns True if that
#integer is an odd number and False if the number is an even number
#Input:  a positive integer, n
#Output: either True or False
#Assumptions: n will be an integer > 1
def isOdd(n):

    #if odd, return False
    for i in range(1, n):
        if n % 2 == 0:
            return False

    #if not odd, then return True
    return True

def main():

    #initiates choice
    choice = ''

    #prints the greeting
    printGreeting()

    #while loop, until the user inputs Q or q, keep running
    while choice != 'Q' and choice != 'q':

        #prints the menu
        printMenu()

        #ask the user for a choice from the menu
        choice = raw_input("Enter your choice: ")

        #if choice is 'I' or 'i', proceed to the next step below
        if choice == 'I' or choice == 'i':

            #gets the value of n
            n = getValidInt(QUES, MIN, MAX)

            #calls hailstone function with the parameter the integer n
            hailstone(n)

        #if choice is 'R' or 'r', proceed to the next step below
        elif choice == 'R' or choice == 'r':

            #calls getValidInt function for the starting and ending values
            start = getValidInt(START_QUES, MIN, MAX)
            end = getValidInt(END_QUES, start + 1, MAX)

            #uses a for loop that gets the value between the starting and
            #ending value
            for i in range(start, end + 1):

                #calls hailstone function with parameter of every number
                #between the starting and ending value
                hailstone(i)

        #if choice is 'L' or 'l', proceed to the next stop below
        elif choice == 'L' or choice == 'l':

            #calls getValidInt function for the starting and ending values
            start = getValidInt(START_QUES, MIN, MAX)
            end = getValidInt(END_QUES, start + 1, MAX)

            #calls longestChain function with the parameter of the starting
            #value and the ending value
            longestChain(start, end)

        #if choice is 'Q' or 'q', quits the program because it makes
        #choice == 'Q' and choice == 'q' from the while loop
        elif choice == 'Q' or choice == 'q':
            print

        #if choice is not any of the choices from above, tell user it
        #was an invalid choice
        else:
            print choice + ' is not a valid choice\n'
    
main()
