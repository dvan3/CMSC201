#Filename:   lab9.py
#Written by: Dave Van
#Date:       4/12/10

# some constants
MIN_YEAR = 1900
MAX_YEAR = 2500
 
SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

NUM_MONTHS = 12
NUM_DAYS   = 7

#printGreeting() greets the user
def printGreeting():
    print "This program will make a calendar."

#printCalendar() prints a calendar
def printCalendar(year):
    for month in range(NUM_MONTHS):
        printMonth(year,month)

def monthName(month):
    print "monthName", month

    return "January"

def firstDayofMonth(month, year):
    print "firstDayofMonth", month, year

    return 3

def indentFirstLine(days):
    print " " * (3 * days - 1),

def monthDays(month, year):
    print "monthDays", month, year

    return 30

def printMonth(year,month):
    name = monthName(month)

    weekday = firstDayofMonth(month, year)

    numDays = monthDays(month, year)

    print "%11s %d" % (name, year)
    print "Su Mo Tu We Th Fr Sa"

    indentFirstLine(weekday)    
    
    for day in range(numDays):
        print "%2d" % (day + 1),

        if weekday == SATURDAY:
            print

        weekday = (weekday + 1) % NUM_DAYS

    if weekday != SUNDAY:
        print

#getValidInt() gets a valid number from the user
def getValidInt(question, min, max):

    # use a bad value to enter the loop
    value = max + 1

    # compose the prompt 
    prompt = question + " (" + str(min) + "-" + str(max) + "): "
    
    # continue to get values until the user enters a valid one
    while value == "" or value < min or value > max:
        value = raw_input(prompt)
        if len(value) != 0:
            value = int(value)

    # return a valid value
    return value



def main():
 
    printGreeting()
 
    year = getValidInt("Which year would you like? ", MIN_YEAR, MAX_YEAR )
    printCalendar(year)

main()
