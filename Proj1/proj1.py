from Airplane import *

#enqueue()
#adds an item passed in the queue, q_items.
#Inputs:  q_items, a queue
#         item,    an item to add in the queue
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
#         item,  an item to push onto the stack
#Outputs: None
def push(s_items, item):

    #adds the item to the stack, s_items
    s_items.append(item)

#pop()
#pops an item from the stack passed in and returns it
#Inputs:  s_items, a stack
#Outputs: popped, the item popped from the stack or print "Phase 2: The tags
#         match in this document" if the stack is empty
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

def top(s_item):
    if len(s_item) == 0:
        return 0
    else:
        return s_item[-1]

# findLargest() finds the largest value in the
# list between start (an index), and stop (an index)
# inclusive, and returns the largest value's index.
#
# Input:  a list to search
#         the 'start'ing and 'stop'ping indices in
#         the list between which to search for the largest
# Output: returns the index corresponding to the largest value
def findLargest(aList, start, stop):

   largestIndex = start
   largestValue = aList[start]

   # look for the largest value in the 
   # unsorted part of the array 
   for i in range(start + 1, stop):
      if (aList[i] > largestValue):
         largestIndex = i
         largestValue = aList[i]

   return (largestIndex)

# selectionSort() selects the largest value
# in the unsorted portion of the list and
# moves it into the current position.  The
# values "swap" positions. 
# Input:    a list to be sorted
# Output:   None, but the list is sorted "in place"
def selectionSort(aList):

   size = len(aList)

   for unsorted in range(size):
       
      largestIndex = findLargest(aList, unsorted, size)

      temp = aList[largestIndex]
      aList[largestIndex] = aList[unsorted]
      aList[unsorted] = temp
      return aList[0]

def main():

    runway1 = []
    runway2 = []
    runway3 = []

    sortList = []

    file1 = "runway1.txt"
    file2 = "runway2.txt"
    file3 = "runway3.txt"

    file = open(file1, 'r')

    for line in file:
        planeName, passengers = line.split();
        plane = Airplane(planeName, passengers)
        push(runway1, plane)

    file = open(file2, 'r')
    
    for line in file:
        planeName, passengers = line.split();
        plane = Airplane(planeName, passengers)
        push(runway2, plane)

    file = open(file3, 'r')

    for line in file:
        planeName, passengers = line.split();
        plane = Airplane(planeName, passengers)
        push(runway3, plane)

    while len(runway1) != 0 and len(runway2) != 0 and len(runway3) != 0:
        plane1 = top(runway1)
        plane2 = top(runway2)
        plane3 = top(runway3)

        sortList = [plane1, plane2, plane3]
        
        size = len(sortList)

        largestPlane = selectionSort(sortList)
        
        print largestPlane.display()
        
main()    
