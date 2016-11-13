#Filename:    hw5.py
#Written by:  Dave Van
#Date:        3/9/10
#Section:     06
#Email:       dvan3@umbc.edu
#Description:
#This program will get a range of numbers from the user and classify whether it
#is an even or odd number; prime, composite or neither; perfect, deficient or
#abundant; square, and triangular.

import sys
import math

#printGreeting prints the greeting that explain what this program does
#Input:  None
#Output: The greeting
def printGreeting():
    print "\nYou will need to enter a number to start from and then a number"
    print "to end. Then the program will classify whether it is an even or odd"
    print "number; prime, composite or neither; perfect, deficient or abundant"
    print "; square, and triangular.\n"
    print "You will now get to choose the range of positive integers that you"
    print "would like to see classified.\n"

#getValidInt() will compose a question for the user and if the user enters an
#integer out of the range, it will keep repeating the question until it is 
#statisfied
#Input:  the question, question; the starting value, min; the ending value, max
#Output: the composed question asking the user for an integer for the starting
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

#printTableHeading prints the heading for the chart
#Input:  None
#Output: The heading
def printTableHeading():
    print "\n Int     Classification................................."
    print "-------------------------------------------------------------------"

#isOdd() takes a positive integer as an argument and returns True if that
#integer is an odd number and False if the number is an even number
#Input:  a positive integer, n
#Output: either True or False
#Assumptions: n will be an integer > 1
def isOdd(n):
    for i in range(1, n):
        if n % 2 == 0:
            return False

    return True
    
#isPrime() takes a positive integer as an argument and returns True if that
#integer is a prime number and False if the number is not prime
#Input:  a positive integer, n
#Output: either True or False
#Assumptions: n will be an integer > 1
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

#isPerfect() takes a positive integer as an argument and returns True if that
#integer is a perfect number;  False if the number is deficient, and nothing
#if the number is abundant
#Input:  a positive integer, n
#Assumptions: n will be an integer > 1
def isPerfect(n):
    x = 1
    sum_of = 0
    while n > x:
        if n % x == 0:
            sum_of += x
        x += 1
    if sum_of == n:
        return True
    elif sum_of < n:
        return False

#isSquare() test if n is a square number
#Input:  a positive integer, n
#Output: a positive integer which is a square number or False if not square
#Assumptions: n will be an integer > 1
def isSquare(n):
    squareCheck = 0
    if n >= 0:
        while squareCheck**2 < n:
            squareCheck += 1
            
        if squareCheck**2 != n:
            return False
        else:
            return True
    else:
        return None

#isTriangular() test if n is a triangular number
#Input:  a positive integer, n
#Output: a positive integer which is a triangle number or False if not triangle
#Assumptions: n will be an integer > 1
def isTriangular(n):
    for i in range(1, n):
        x = (math.sqrt(8*n + 1) - 1) / 2
        if x - int(x) > 0:
            return False
        else:
            return True

#printTableLine() prints out the results of all of the functions above.
#Input:  the starting number, start; a positive integer, n; whether it is odd
#or even, odd; whether it is perfect, deficient or abundant, perfect; whether
#it is a square number, square; and if it is a triangular number, triangular
#Output: a string of what each number is
def printTableLine(start, n):
    for i in range(start, n + 1):
        

        #If the number is True, then pring odd, if not print even
        if isOdd(i) == True:
            evenodd = "Odd"
        else:
            evenodd = "Even"

        #If the number is True, then print prime, if not print composite
        if isPrime(i) == True:
            ifprime = "Prime"
        else:
            ifprime = "Composite"

        #If the number is True, print Square, if not print nothing
        if isSquare(i) == True:
            square = "Square"
        else:
            square = " "

        #If the number is True, print Perfect, else if False, print Deficient
        #else, print Abundant
        if isPerfect(i) == True:
            perfect = "Perfect"
        elif isPerfect(i) == False:
            perfect = "Deficient"
        else:
            perfect = "Abundant"
            
        #If the number is True, then it is Triangular, if not then blank
        if isTriangular(i) == False:
            triangle = " "
        else:
            triangle = "Triangular"

        if i == 1:
            ifprime = "Neither"

        #Prints the chart
        print "%3d %10s %12s %14s %9s %12s" % (i, evenodd, ifprime
                                           ,perfect , square, triangle)
        
def main():
    
    printGreeting()

    START_QUES = "Please enter a starting integer"
    END_QUES = "Please enter an ending integer"

    start = getValidInt(START_QUES, 1, 100000)
    end = getValidInt(END_QUES, start, 100000)
      
    #Gets the value of n
    for i in range(start, end + 1):
        n = i

    printTableHeading()
    printTableLine(start, n)
    
main()
