#File:    hw4.py
#Author:  Dave Van
#Date:    3/3/10
#Section: 06
#E-mail:  dvan3@umbc.edu
#Description:
#This file contains python code that will tell
#user what CMSC courses they are required to take
#order to complete the Computer Science major at UMBC.

def main():
    
    #Greeting
    print "This program will tell you what courses you need to take"
    print "in order to complete the Computer Science major at UMBC.\n"
    
    #List for CMSC class taken
    cmsc_class = []
    
    #List for MATH class taken
    math_class = []
    
    #Computer science required courses in a list(extended and appended)
    part_a = ['CMSC 201', 'CMSC 202', 'CMSC 203', 'CMSC 304', 'CMSC 313']
    part_a.extend(['CMSC 331', 'CMSC 341', 'CMSC 345', 'CMSC 411', 'CMSC 421'])
    part_a.append('CMSC 441')

    #Math required courses in a list
    part_b = ['MATH 151', 'MATH 152', 'MATH 221']

    #Gets how many CMSC classes the user has taken
    cmsc_taken = input("How many CMSC Classes have you taken? ")

    #Instructs the user how to enter the information
    print "\nEnter class in the form <MAJOR-CODE> <COURSE-NUMBER> "

    #User inputs the class name and number for how many classes they have taken
    #and puts it in the corresponding list
    for i in range(cmsc_taken):    
        cmsc_course = raw_input("Class: ")
        cmsc_class.append(cmsc_course)

    #Gets how many MATH classes the user has taken
    math_taken = input("\nHow many MATH Classes have you taken? ")

    #Instructs the user how to enter the information
    print "\nEnter class in the form <MAJOR-CODE> <COURSE-NUMBER> "

    #User inputs the class name and number for how many classes they have taken
    #and puts it in the corresponding list
    for i in range(math_taken):
        math_course = raw_input("Class: ")
        math_class.append(math_course)

    #Gets input from user for STAT class
    stat = raw_input("\nHave you taken STAT 355 or STAT 451?(YES or NO): ")
        
    #Check if CMSC list works
    #print "\nTHIS IS A CHECK IF THE CMSC LIST WORKS"
    #for i in range(cmsc_taken):
    #    print cmsc_class[i]

    #Check if MATH list works
    #print "\nTHIS IS A CHECK IF THE MATH LIST WORKS"
    #for i in range(math_taken):
    #    print math_class[i]

    #Removes the classes the user has taken from cmsc_class from part_a and
    #then it prints out the left over classes
    print "\nPart A Requirements"
    for i in range(len(cmsc_class)):
        part_a.remove(cmsc_class[i])
    if len(part_a) == 0:
        print "You have completed Part A"
    else:
        for i in range(len(part_a)):
            print "You need to take " + part_a[i]

    #Removes the classes the user has taken from math_class from part_b and
    #then it prints out the left over classes
    print "\nPart B Requirements"
    for i in range(len(math_class)):
        part_b.remove(math_class[i])
    if len(part_b) == 0:
        print "You have completed Part B"
    else:
        for i in range(len(part_b)):
            print "You need to take " + part_b[i]

    #If the input from stat is YES then they have completed part C, if NO
    #Then they need to take one of the two STAT classes avaiable
    print "\nPart C Requirements"
    if stat == 'YES':
        print "You have completed Part C"
    else:
        print "You need to take STAT 355 or STAT 451\n"
    
main()
