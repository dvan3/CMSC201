#Filename:   lab11.py
#Written by: Dave Van
#Date:       4/26/10


import random
import time

def linearSearch(numbers, find):

    for i, x in enumerate(numbers):
        if x == find:
            return i

    return -1


def binarySearch(numbers, find):

    low = 0
    high = len(numbers) - 1

    while low <= high:

        mid = (low + high) / 2
       
        if find == numbers[mid]:
            return mid
       
        elif find > numbers[mid]:
            low = mid + 1
       
        else:
            high = mid - 1

    return -1


def main():

    size = input("Enter list size: ")

    numbers = range(size)

    t0 = time.time()

    random.shuffle(numbers)

    for i in xrange(1000):
        find = random.randint(0, size - 1)

        found = linearSearch(numbers, find)

        if found == -1:
            print "ERROR: didn't find number in linearSearch!"

    t1 = time.time()

    numbers.sort()
    for i in xrange(1000):
        find = random.randint(0, size - 1)

        found = binarySearch(numbers, find)

        if found == -1:
            print "ERROR: didn't find number in binarySearch!"

    t2 = time.time()

    linearTime = t1 - t0
    binaryTime = t2 - t1

    print "Linear time: ", linearTime
    print "Binary time: ", binaryTime
    
main()
