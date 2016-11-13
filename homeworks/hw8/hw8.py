#Filename:    hw8.py
#Written by:  Dave Van
#Date:        4/12/10
#Section:     06
#Email:       dvan3@umbc.edu
#Description:
#This is a "World Traveler" program that will allow the user to perform
#conversions from four currencies into US dollars, calculate the time of day
#(Eastern Standard Time) from the time in each of the 5 cities visited, and
#also convert celsius temperatures into fahrenheit temperatures.

#constants
#question constants
CHOICE_QUES    = "Your choice"
POUNDS_QUES    = "How many Pounds? "
KRONOR_QUES    = "How many Kronors? "
EUROS_QUES     = "How many Euros? "
RUBLES_QUES    = "How many Rubles? "
HOUR_QUES      = "Enter the hour "
MINUTE_QUES       = "Enter the minute "
#choice constants
MIN            = 1
MAX            = 4
#time constants
HOUR_MIN       = 0
HOUR_MAX       = 23
MINUTE_MIN     = 0
MINUTE_MAX     = 59
LONDON_TIME    = 5
STOCKHOLM_TIME = 6
TAMP_HEL_TIME  = 7
ST_PETER_TIME  = 8
HOUR_DIFF      = 12
#money constants
BAD_START      = -1
DOLLAR_POUND   = 1.53730
DOLLAR_KRONOR  = 0.139083
DOLLAR_EURO    = 1.34960
DOLLAR_RUBLE   = 0.0343348
#temperature constants
F_TOP          = 9.0
F_BOTTOM       = 5.0
F_FREEZE       = 32
#menu constants
MENU_TIME      = 1
MENU_CURRENCY  = 2
MENU_TEMP      = 3
MENU_QUIT      = 4

#printGreeting() displays a suitable greeting to the user
#Input:  none
#Output: the greeting
def printGreeting():
    print "\nThis program is the World Traveler program that will allow the"
    print "user to perform conversions from four currencies into US dollars,"
    print "calculates the time of day (Eastern Standard Time) from the time"
    print "in each of the 5 cities visited, and also convert celsius"
    print "temperatures into fahrenheit temperature\n"

#displayMainMenu() displays the main menu choices
#Input:  none
#Output: the main menu
def displayMainMenu():
    print "\t1 - Time"
    print "\n\t2 - Currency"
    print "\n\t3 - Temperature"
    print "\n\t4 - QUIT\n"

#displayLocationsMenu() displays the location menu choices
#Input:  none
#Output: the location menu
def displayLocationsMenu():
    print "\nChoose a location or M to return to Main Menu\n"
    print "\tL - London"
    print "\n\tS - Stockholm"
    print "\n\tT - Tampere"
    print "\n\tH - Helsinki"
    print "\n\tP - St. Petersburg"
    print "\n\tM - Return to Main Menu\n"

#getValidInt() prompts the user and gets an integer from the user between
#min and max, inclusive and returns that valid integer
#Input:  question, minimum, maximum
#Output: the value
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

    #return valid value
    return value

#getValidTime() returns a time between 00:00 and 23:59, inclusive, as an hour
#minute tuple
#Input:  none
#Output: a valid hour and minute
def getValidTime():

    #gets a value for hour
    hour = getValidInt(HOUR_QUES, HOUR_MIN, HOUR_MAX)

    #gets a value for min
    min  = getValidInt(MINUTE_QUES, MINUTE_MIN, MINUTE_MAX)

    #return hour and minutes
    return hour, min

#getPositiveReal gets a positive real number
#Input:  a question
#Output: a value positive real number 
def getPositiveReal(question):

    #use a bad value to start the loop
    units = BAD_START

    #continue to get values until the user enters a valid one 
    while units < 0 or units == "":
        units = raw_input(question)
        if len(units) != 0:
            units = float(units)

    #return a value number
    return units

#convertTime() is a top level function that handles the user input, processing,
#and output dealing with converting time
#Input:  none
#Output: the location menu and the converted time
def convertTime():

    #initialize choice
    choice2 = ''

    #keep running the loop until the user enters 'M' or 'm' to stop the program
    while choice2 != 'M' and choice2 != 'm':

        #calls displayLocationsMenu function
        displayLocationsMenu()

        #gets a menu choice from the user
        choice2 = raw_input("Enter a location or M to return to Main "
                            "Menu: ")

        #if user chooses 'L' or 'l' proceed with the following
        if choice2 == 'L' or choice2 == 'l':

            #get the hour and minute
            hour, min = getValidTime()

            #get the new converted time and whether it is AM or PM
            newHour, display = foreignTimeToEastern (hour, LONDON_TIME)

            #print the new converted time
            print "\n%02d:%02d in London is %d:%02d %s" % (hour, min, newHour
                                                             , min, display)

        #if user chooses 'S' or 's' proceed with the following
        elif choice2 == 'S' or choice2 == 's':

            #get the hour and minute
            hour, min = getValidTime()

            #get the new converted time and whether it is AM or PM
            newHour, display = foreignTimeToEastern (hour, STOCKHOLM_TIME)

            #print the new converted time
            print "\n%02d:%02d in Stockholm is %d:%02d %s" % (hour, min,
                                                                newHour, min,
                                                                display)

        #if user chooses 'T' or 't' proceed with the following
        elif choice2 == 'T' or choice2 == 't':

            #get the hour and minute
            hour, min = getValidTime()

            #get the new converted time and whether it is AM or PM
            newHour, display = foreignTimeToEastern (hour, TAMP_HEL_TIME)

            #print the new converted time
            print "\n%d:%02d in Tampere is %d:%02d %s" % (hour, min, newHour,
                                                          min, display)

        #if user chooses 'H' or 'h' proceed with the following
        elif choice2 == 'H' or choice2 == 'h':

            #get the hour and minute
            hour, min = getValidTime()

            #get the new converted time and whether it is AM or PM
            newHour, display = foreignTimeToEastern (hour, TAMP_HEL_TIME)

            #print the new converted time
            print "\n%02d:%02d in Helsinki is %d:%02d %s" % (hour, min,
                                                               newHour, min,
                                                               display)

        #if user chooses 'P' or 'p' proceed with the following
        elif choice2 == 'P' or choice2 == 'p':

            #get the hour and minute
            hour, min = getValidTime()

            #get the new converted time and whether it is AM or PM
            newHour, display = foreignTimeToEastern (hour, ST_PETER_TIME)

            #print the new converted time
            print "\n%02d:%02d in St. Petersburg is %d:%02d %s" % (hour, min,
                                                         newHour, min, display)

        #if user chooses 'M' or 'm' return to main menu
        elif choice2 == 'M' or choice2 == 'm':
            print

        #if user entered a invalid choice, tell the user that it is invalid
        else:
            print choice2 + ' is not a valid choice'

#foreignTimeToEastern() converts the 24 hour time to a 12 hour time and
#adjusts the time zone and whether it is AM or PM
#Input:  the hour, and the adjustment time zone
#Output: the new converted hour and the time of the day
def foreignTimeToEastern (hour, adjustment):

    #gets the new adjusted hour
    hour = hour - adjustment

    #if the new hour is less than 0 add 12 to the hour
    if 1 > hour:

        #add 12 to the hour
        hour += HOUR_DIFF

        #store the time of the day prior
        display = "PM EST of the prior day"

    #if the new hour is greater than 12 subtract 12 to the hour
    elif hour > HOUR_DIFF:

        #subtract the hour by 12
        hour = hour - HOUR_DIFF

        #store the time of the day
        display = "PM EST"

    #if none of the above, just print AM
    else:
        display = "AM EST"

    #returns the convert hour and whether it is AM or PM
    return hour, display

#convertCurrency() is a top level function that handles all of the user input,
#processing, and output dealing with converting currency
#Input:  none
#Output: the location menu, and the converted currency
def convertCurrency():

    #initialize choice
    choice2 = ''

    #keep running the loop until the user enters 'M' or 'm' to stop the program
    while choice2 != 'M' and choice2 != 'm':

        #calls the displayLocationMenu function
        displayLocationsMenu()

        #gets menu choice from the user
        choice2 = raw_input("Enter a location or M to return to Main "
                            "Menu: ")

        #if user chooses 'L' or 'l' proceed with the following
        if choice2 == 'L' or choice2 == 'l':

            #gets a positive real number
            units = getPositiveReal(POUNDS_QUES)

            #gets the converted currency from foreign to US dollars
            dollars = foreignToDollars(units, DOLLAR_POUND)

            #prints the new converted currency
            print
            print "%.2f pounds is $ %.2f" % (units, dollars)

        #if user chooses 'S' or 's' proceed with the following
        elif choice2 == 'S' or choice2 == 's':

            #gets a positive real number
            units = getPositiveReal(KRONOR_QUES)

            #gets the converted currency from foreign to US dollars
            dollars = foreignToDollars(units, DOLLAR_KRONOR)

            #prints the new converted currency
            print
            print "%.2f Kronors is $ %.2f" % (units, dollars)

        #if user chooses 'T' or 't' proceed with the following
        elif choice2 == 'T' or choice2 == 't':

            #gets a positive real number
            units = getPositiveReal(EUROS_QUES)

            #gets the converted currency from foreign to US dollars
            dollars = foreignToDollars(units, DOLLAR_EURO)

            #prints the new converted currency
            print
            print "%.2f Euros is $ %.2f" % (units, dollars)

        #if user chooses 'H' or 'h' proceed with the following
        elif choice2 == 'H' or choice2 == 'h':

            #gets a positive real number
            units = getPositiveReal(EUROS_QUES)

            #gets the converted currency from foreign to US dollars
            dollars = foreignToDollars(units, DOLLAR_EURO)

            #prints the new converted currency
            print
            print "%.2f Euros is $ %.2f" % (units, dollars)

        #if user chooses 'P' or 'p' proceed with the following
        elif choice2 == 'P' or choice2 == 'p':

            #gets a positive real number
            units = getPositiveReal(RUBLES_QUES)

            #gets the converted currency from foreign to US dollars
            dollars = foreignToDollars(units, DOLLAR_RUBLE)

            #prints the new converted currency
            print
            print "%.2f Rubles is $ %.2f" % (units, dollars)

        #if user chooses 'M' or 'm' return to main menu
        elif choice2 == 'M' or choice2 == 'm':
            print

        #if user entered a invalid choice, tell the user that it is invalid
        else:
            print choice2 + ' is not a valid choice'

#foreignToDollars() accepts the number of units of a foreign currency and a
#conversion factor and returns the equivalent number of US dollars
#Input:  the foreign currency, and the convertion rate
#Output: the converted US dollars
def foreignToDollars(units, conv):

    #converts the foreign currecny to US dollars
    convertDollars = units * conv

    #returns US dollars
    return convertDollars
    
#convertTemp() is a top level function that handles all of the user input,
#processing, and output dealing with converting temperature
#Input:  none
#Output: the converted temperature
def convertTemp():

    #gets the celsius temperature
    celsius = input("What is the Celsius temperature? ")

    #converts celsius to fahrenheit
    fahrenheit = celsiusToFahrenheit(celsius)

    #prints the converted temperature
    print "The temperature is ", fahrenheit, "degrees in fahrenheit\n"

#celsiusToFahrenheit() returns the fahrenheit equivalent of the celsius
#temperature passed in
#Input:  the celsius temperature
#Output: the fahrenheit temperature
def celsiusToFahrenheit(celsius):

    #converts to fahrenheit temperature
    fahrenheit = (F_TOP / F_BOTTOM) * celsius + F_FREEZE

    #returns the fahrenheit temperature
    return fahrenheit

def main():

    #initialize choice
    choice = ''

    #calls the printGreeting function
    printGreeting()

    #continue showing the menu until the user quits the program
    while choice != MENU_QUIT:

        #calls the displayMainMenu function
        displayMainMenu()

        #gets a valid choice from the user
        choice = getValidInt(CHOICE_QUES, MIN, MAX)

        #if the user chooses '1' proceed with the convertTime function
        if choice == MENU_TIME:

            #calls convertTime function
            convertTime()

        #if the user chooses '2' proceed with the convertCurrency function
        elif choice == MENU_CURRENCY:

            #calls convertCurrency function
            convertCurrency()

        #if the user chooses '3' proceed with the convertTemp function
        elif choice == MENU_TEMP:

            #calls convertTemp function
            convertTemp()

        #if the user chooses '4' quit the program
        elif choice == MENU_QUIT:
            print

        #if the user doesn't input a valid value, continue with the menu
        else:
            print choice + ' is not a valid choice\n'
                                                            
main()
