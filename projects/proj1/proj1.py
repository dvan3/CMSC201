#Filename: proj1.py
#Author:   Dave Van
#Date:     4/21/10
#Email:    dvan3@umbc.edu
#Section:  06
#
#This program will read from a file and print an analysis of the file to the
#screen. The sequence of tags in the file will be echoed to the output; any
#other text in the file is to be ignored. If there is a tag balancing error or 
#the program reaches the end of the file while in the middle of a tag, the 
#program must quit and print an error message. If the end of fileis reached
#without any errors, print a message to that effect.

import sys

#constants
NUM_ARGS   = 2
INDEX      = 2
START      = "<"
END        = ">"
CLOSE      = "/"
NOTFILE    = ".dat"

#printGreeting()
#displays a greeting and explanation of the program to the user
#Inputs:  None
#Outputs: None
def printGreeting():
    
    print 
    print "This program will read a file and print the analysis of the file to"
    print "the screen. The sequence of the tags in the file will be echoed to"
    print "the output; any other text in the fiel is to be ignored. If there"
    print "is a tag balancing error or the program reaches the end of the file"
    print "while in the middle of a tag, the program must quit and print an"
    print "error message. If the end of the file is reached without any"
    print "errors, print a message to that effect."
    print

#enqueue()
#adds an item passed in the queue, q_items.
#Inputs:  q_items, a queue
#	  item,    an item to add in the queue
#Outputs: None
def enqueue(q_items, item):

     #add the item into the queue, q_items
    q_items.append(item)

#dequeue()
#removes the first item that got added into the queue from the queue and
#returns it
#Inputs:  q_items, a queue
#Outputs: dequeued, the item that was removed from the queue.
def dequeue(q_items):

    #get the size of the queue
    size = len(q_items)

    #keep removing the first item in the queue from the queue until the
    #size of the queue is 0
    if size >  0:
        dequeued = q_items[0]
        del(q_items[0])
        return dequeued
    else:
        return "Empty queue"

#push()
#pushes the item passed in onto the stack passed in, s_items.
#Inputs:  s_items, a stack
#	  item,  an item to push onto the stack
#Outputs: None
def push(s_items, item):

    #adds the item to the stack, s_items
    s_items.append(item)

#pop()
#pops an item from the stack passed in and returns it
#Inputs:  s_items, a stack
#Outputs: popped, the item popped from the stack or print "Phase 2: The tags 
#	  match in this document" if the stack is empty
def pop(s_items):

    #gets the size of the stack
    size = len(s_items)

    #keep removing the last item from the stack until the size of the stack
    #reaches 0
    if size > 0:
        popped = s_items[- 1]
        del(s_items[- 1])
        return popped
    else:
        return "Empty Stack"
    
#fileOpen()
#opens the file
#Inputs:  None
#Outputs: opens the file
def fileOpen():

    #opens the second argument in the commandline
    file = open(sys.argv[1], "r")

    #returns the opened file
    return file

#fileClose()
#closes the file
#Inputs:  file, the opened file
#Outputs: closes the file
def fileClose(file):

    #closes the file
    file.close()

#compare()
#compares the tags of the html code and prints the results
#Inputs:  tag, the tag dequeued from the queue; popTag, the tag from the stack
#Outputs: prints which tags matches else exit the system
def compare(tag, popTag):

    #if the tags matches, print that it matches else, print there is an error
    #and exit the program
    if popTag[1 : len(popTag) - 1] == tag[INDEX : len(tag) - 1]:
        print popTag + " matches " + tag
    else:
        print "There is a balancing issue with the html code"
        sys.exit()

#phaseOne()
#enqueues all of the tags in the html file
#Inputs:  file, the opened file; q_items, the queue
#Outputs: None
def phaseOne(file, q_items):
    
    #for every line in the file
    for line in file:

        #for every character in the length of the line
        for i in range(len(line)):

            #finds whether there is a < in the line
            if line[i] == START:
                start = i

            #finds whether there is a > in the line
            if line[i] == END:
                end = i + 1

                #indexs the starting < through the ending >
                tag = line[start : end]
                print tag

                #calls the function enqueue()
                enqueue(q_items, tag)

    #prints that the file had no errors
    print "Phase 1: End of file was reached for", sys.argv[1],
    print "with no errors."
    print

#phaseTwo()
#finds the starting tag and ending tag and compares if they are matching
#Inputs:  q_items, the queue; s_items, the stack
#Outputs: None
def phaseTwo(q_items, s_items):

    #while the length of the queue is not 0 keep dequeuing
    while len(q_items) != 0:
        tag = dequeue(q_items)

        #if the tag is a starting tag push into the stack
        if tag.find(CLOSE) == -1:

            #calls the function push()
            push(s_items, tag)

        #if the tag is a closing tag pop it out of the stack
        elif tag.find(CLOSE) == 1:
            popTag = pop(s_items)

            #calls the function compare()
            compare(tag, popTag)
        else:

            #print the results
            print tag + " is self-closing"

    #Phase 2 has matching tags
    print "Phase 2: The tags match in this document"
    
    

def main():

    #the queue
    q_items = []

    #the stack
    s_items = []

    #if the user enters more than 2 command arguments exit the program
    if len(sys.argv) != NUM_ARGS:
        print
        print "This program requires command line arguments."
        print "The first argument is the executable file."
        print "The second argument is the name of the html file."
        print 
        sys.exit()

    #sets the second commandline argument into a variable
    argSys = sys.argv[1]

    #checks if the file is a .dat file
    if argSys[-4 :] != NOTFILE:
        print "Not a html file"
        sys.exit()

    #opens the file
    file = fileOpen()

    #calls the function printGreeting()
    printGreeting()

    #calls the function phaseOne()
    phaseOne(file, q_items)

    #closes the opened file
    fileClose(file)

    #calls the functino phaseTwo()
    phaseTwo(q_items, s_items)
            
main()
