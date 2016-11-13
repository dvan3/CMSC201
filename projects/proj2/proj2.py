#Filename: design2.txt
#Author:   Dave Van
#Date:     5/6/10
#Email:    dvan3@umbc.edu
#Section:  06
#Description:
#This program will use recursive functions to draw a koch snowflake, a
#C-Curve, an animated koch snowflake, and a dragon curve. It will also
#use a user defined turtle class to draw the snowflakes and curves.

from graphics import *
from time import sleep
import math

#Constants
#Menu constants
UP_KOCH       = 'K'
UP_CCURVE     = 'C'
UP_ANIMATE    = 'A'
UP_MENU_QUIT  = 'Q'
LOW_KOCH      = 'k'
LOW_CCURVE    = 'c'
LOW_ANIMATE   = 'a'
LOW_MENU_QUIT = 'q'
UP_D_CURVE    = 'D'
LOW_D_CURVE   = 'd'
#Degree constants
DEGREE_Z     = 0
DEGREE_O     = 1
DEGREE_T     = 2
DEGREE_THR   = 3
DEGREE_F     = 4
C_DEGREE     = 12
#Length
LENGTH       = 243
LENGTHDIV    = 3
SQUAREROOT   = 2
#valid int constants
MIN          = 0
MAX          = 4
QUESTION     = "What degree snowflake? "
COLOR        = "What color snowflake? "
#Angle constants
ACUTE        = 45
NEG_ACUTE    = -45
HALF_ACUTE   = 60
RT_ANGLE     = 90
NEG_RT_ANGLE = -90
NEG_OBTUSE   = -120
HALF_CIRC    = 180.0
#Colors
BLACK        = 'black'
GOLD         = 'gold'
RED          = 'red'
GREEN        = 'green'
BLUE         = 'blue'
#Dragon
DRAGON_COLOR = 'OrangeRed2'
DRAGON_CRY   = 'gold'
DRAGON_CURVE = 12
DRAGON_LEN   = 300
DRAGON_MAG   = 1.41421356237
FLIP_NEG     = -1
FLIP         = 1

#the turtle class
class Turtle:
    """A class defining a turtle that draws a line where it goes."""

    #converts degrees to radians
    degtoRad = math.pi / HALF_CIRC

    #constructor
    def __init__(self, position, direction, window, color):
        """Initialize a turtle with given position, direction, window,
        colors"""

        #initiates the arguments
        self.position = position
        self.direction = float(direction)
        self.window = window
        self.color = color

    #Accessors
    def getPosition(self):
        """Gets the position of the turtle"""

        #returns the position
        return self.position

    def getDirection(self):
        """Gets the direction of which the turtle is facing"""

        #returns the direction
        return self.direction

    #Methods
    def forward(self, distance):
        """Moves the turtle forward for the distance given and draws a line
        as it moves"""

        #get the current X and Y positions
        currentY = self.position.getY()
        currentX = self.position.getX()

        #get the point to where the turtle is going to move to
        dx = distance * math.cos(self.direction * self.degtoRad)
        dy = distance * math.sin(self.direction * self.degtoRad)

        #gets the new X and Y
        newX = currentX + dx
        newY = currentY + dy

        #Gets a new point by using the new X and Y points
        newPoint = Point(newX, newY)

        #Makes a line with the current position and its new point
        newLine = Line(self.position, newPoint)

        #sets the color of the line
        newLine.setOutline(self.color)

        #draws the line on the window
        newLine.draw(self.window)

        #sets the new point to its currect position
        self.position = newPoint
        
    def turn(self, degrees):
        """Turns the turtle to the degrees given"""

        #adds the degrees given to the current direction
        self.direction += degrees

#printGreeting()
#displays a greeting and explanation of the program to the user
#Inputs:  None
#Outputs: None
def printGreeting():
    print "\nThe user will choose a menu option to draw a koch snowflake"
    print "at a degree and color the user chooses, or to draw a c-curve drawn"
    print "at the 12th degree, or to draw a animated koch snowflake from"
    print "degree 0 to degree 4 or the user can choose to draw a dragon curve"
    print

#displayMenu()
#displays the menu choices
#Inputs:  None
#Outputs: None
def displayMenu():
    print "\tK - view the Koch Snowflake"
    print "\n\tC - view the C-Curve"
    print "\n\tA - view the Animated Koch Snowflake"
    print "\n\tD - view the Dragon Curve"
    print "\n\tQ - Quit"
    print 

#kochFlake()
#a function that calls the drawKoch() function to draw the koch snowflake
#Inputs:  color, the color used
#         degree, the degree of the koch
#         window, a window
#Outputs: None
def kochFlake(color, degree, window):

    #makes the turtle maxwell on the window
    maxwell =  Turtle(Point(125,300),0, window, color) 

    #sets the length
    length = LENGTH

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

    #turns the turtle -120 degrees right
    maxwell.turn(NEG_OBTUSE)

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

    #turns the turtle -120 degrees right
    maxwell.turn(NEG_OBTUSE)

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

#levycCurve()
#calls the function cCurve() to draw the C-Curve
#Inputs:  color, the color used
#         degree, the degree of the curve
#         window, a window
#Outputs: None
def levycCurve(color, degree, window):

    #makes the turtle on the window
    maxwell = Turtle(Point(150, 150), 0, window, color)

    #sets the length
    length = LENGTH

    #turns the turtle -90 degrees right
    maxwell.turn(NEG_RT_ANGLE)

    #calls the function cCurve()
    cCurve(maxwell, length, degree, color)

#cCurve()
#a recursive function that draws the C-Curve
#Inputs:  maxwell, the turtle
#         length, the length of the line
#         degree, the degree of the line
#         color, the color used
#Outputs: it will draw the C-Curve
def cCurve(maxwell, length, degree, color):

    #base case
    if degree == 0:

        #move the turtle to the length give forward
        maxwell.forward(length)
        return 1

    #general rule
    else:

        #turn the turtle 45 degrees left
        maxwell.turn(ACUTE)

        #calls itself with minus 1 degree
        cCurve(maxwell, length / math.sqrt(SQUAREROOT), degree - 1, color)

        #turn the turtle 90 degrees left
        maxwell.turn(RT_ANGLE)

        #calls itself with minus 1 degree
        cCurve(maxwell, length / math.sqrt(SQUAREROOT), degree - 1, color)

        #turn the turtle 45 degrees left
        maxwell.turn(ACUTE)

#animateKoch()
#a function that calls drawKoch() to animate degree 0 through degree 4
#of the koch
#snowflake
#Inputs:  color, the color used
#         degree, the degree of the line
#         window, a window
#Outputs: it will animate the koch snowflake from degree 0 to degree 4
def animateKoch(color, degree, window):

    #makes the turtle
    maxwell = Turtle(Point(125, 300), 0, window, color)

    #sets the length
    length = LENGTH

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

    #turn the turtle -120 degrees right
    maxwell.turn(NEG_OBTUSE)

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

    #turn the turtle -120 degrees right
    maxwell.turn(NEG_OBTUSE)

    #calls the function drawKoch()
    drawKoch(maxwell, length, degree, color)

#getValidInt()
#prompts the user and gets an integer from the user between 0 through 4
#Inputs:  question, the question to be used
#         min, the minimum value accepted
#         max, the maximum value accepted
#Outputs: a valid value
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

#getValidColor()
#prompt the user and gets a valid color
#Inputs:  question, the question to be used
#         color_list, the list of colors accepted
#Outputs: a valid color
def getValidColor(question, color_list):

    #prints out the list of colors the user can choose from
    print "\nChoose a color for your Koch Snowflake\n"
    for i in color_list:
        print "%15s" % i
    print

    #using a bad color to start the loop
    color = 'white'

    #the question to be asked
    prompt = question

    #until the user enters a valid color keep asking for a color
    while color not in color_list:
        color = raw_input(prompt)

        #converts color to all lower cases
        color = color.lower()
        print 
        if len(color) != 0:
            color = str(color)

    #returns a valid color
    return color

#drawKoch()
#draws the koch snowflake to the chosen degree
#Inputs:  maxwell, the turtle
#         length, the length of the line
#         degree, the degree of the line
#         color, the color used
#Outputs: the koch snowflake to the degree chosen
def drawKoch(maxwell, length, degree, color):

    #base case
    if degree == 0:

        #move the turtle forwards to the length given
        maxwell.forward(length)
        return 1

    #general rule
    else:

        #calls itself with minus 1 degree
        drawKoch(maxwell, length / LENGTHDIV, degree - 1, color)

        #turn the turtle 60 degrees left
        maxwell.turn(HALF_ACUTE)

        #calls itself with minus 1 degree
        drawKoch(maxwell, length / LENGTHDIV, degree - 1, color)

        #turn the turtle -120 degrees right
        maxwell.turn(NEG_OBTUSE)

        #calls itself with minus 1 degree
        drawKoch(maxwell, length / LENGTHDIV, degree - 1, color)

        #turn the turtle 60 degrees left
        maxwell.turn(HALF_ACUTE)

        #calls itself with minus 1 degree
        drawKoch(maxwell, length / LENGTHDIV, degree - 1, color)

#callDragon()
#calls the dragon function inorder to draw the dragon curve
#Inputs:  color, the color used
#         degree, the degree of the curve
#         window, a window
#Outputs: None
def callDragon(color, degree, window):

    #makes the turtle
    maxwell = Turtle(Point(175, 75), 0, window, color)

    #sets the length
    length = DRAGON_LEN
    
    side = 1

    #turn the turtle 90 degrees left
    maxwell.turn(RT_ANGLE)

    #calls the function dragon()
    dragon(maxwell, length, degree, color, side)

#dragon()
#draws the dragon curve to the 12th degree
#Inputs:  maxwell, the turtle
#         length, the length of the line
#         degree, the degree of the curve
#         color, the color used
#         side, the side of the line
#Outputs: the drawn dragon curve
def dragon(maxwell, length, degree, color, side):

    #base case
    if degree > 0:

        #turn the turtle -45 * 1 degrees right
        maxwell.turn(NEG_ACUTE * side)

        #calls itself with minus 1 degree, and makes the side negative
        dragon(maxwell, length/DRAGON_MAG, degree - 1, color, FLIP_NEG)

        #turn the turtle 90 * 1 degrees left
        maxwell.turn(RT_ANGLE * side)

        #calls itself with minus 1 degree, and makes the side positive
        dragon(maxwell, length/DRAGON_MAG, degree - 1, color, FLIP)

        #turn the turtle -45 * 1 degrees right
        maxwell.turn(NEG_ACUTE * side)

        #general rule
    else:
        #move the turtle forwards to the length given
        maxwell.forward(length)
    
def main():

    #list of colors that the user can choose from
    color_list = ['blue', 'brown', 'gold', 'green', 'black', 'red', 'purple']

    #initiate choice
    choice = ''

    #calls the function printGreetin()
    printGreeting()

    #keep running the menu until the user quits
    while choice != UP_MENU_QUIT and choice != LOW_MENU_QUIT:

        #calls the function displayMenu()
        displayMenu()

        #prompts the user for a menu choice
        choice = raw_input("Enter your choice: ")
        print 

        #if user chooses 'K' or 'k' proceed with the choice
        if choice == UP_KOCH or choice ==LOW_KOCH:

            #gets the degree by calling getValidInt()
            degree = getValidInt(QUESTION, MIN, MAX)

            #gets the color by calling getValidColor()
            color = getValidColor(COLOR, color_list)
            
            #creates a window
            window = GraphWin("Koch Snowflake", 500, 500)

            #calls the function kochFlake()
            kochFlake(color, degree, window)

        #if user chooses 'C' or 'c' proceed with the choice
        elif choice == UP_CCURVE or  choice == LOW_CCURVE:

            #sets the degree to 12
            degree = C_DEGREE

            #sets the color to black
            color = BLACK

            #creates a window
            window = GraphWin("C-Curve on the 12th degree", 550, 500)

            #calls the function levycCurve()
            levycCurve(color, degree, window)

        #if user chooses 'A' or 'a' proceed with the choice
        elif choice == UP_ANIMATE or choice == LOW_ANIMATE:

            #creates a window
            window = GraphWin("Animated Koch Snowflake", 500, 500)

            #calls the function animateKoch with the approriate color, degree,
            #and a window. Between each degree, pause the program for 1 second
            #then proceed on with the drawing
            animateKoch(GOLD, DEGREE_Z, window)
            sleep(1.0)
            animateKoch(GREEN, DEGREE_O, window)
            sleep(1.0)
            animateKoch(BLUE, DEGREE_T, window)
            sleep(1.0)
            animateKoch(RED, DEGREE_THR, window)
            sleep(1.0)
            animateKoch(BLACK, DEGREE_F, window)

        #if user chooses 'D' or 'd' proceed with the choice
        elif choice == UP_D_CURVE or choice == LOW_D_CURVE:

            #creates a window
            window = GraphWin("Dragon Curve", 500, 500)

            #makes a text on the window
            dragonCry = Text(Point(350, 75), "Fear the Dragon!!")

            #sets the color of the text
            dragonCry.setOutline(DRAGON_CRY)

            #draws the text on the window
            dragonCry.draw(window)

            #sets the color to orange
            color = DRAGON_COLOR

            #sets the degree to 12
            degree = DRAGON_CURVE

            #calls the function callDragon()
            callDragon(color, degree, window)

        elif choice == 'T' or choice == 't':

            window = GraphWin("TriForce", 500, 500)

            color = DRAGON_CURVE

            degree = HALF_ACUTE

            callTriForce(color, degree, window)

        #if user chooses 'Q' or 'q' proceed with the choice
        elif choice == UP_MENU_QUIT or choice == LOW_MENU_QUIT:
            print

        #if the choice is not valid, print error message
        else:
            print choice + ' is not a valid choice\n'
            

main()
