#Filename:   die.py
#Written by: Dave Van
#Date:       5/10/10

import random

class Die:
    def __init__(self, sides):
        #Just copy over the sides value
        self.sides = sides
        
    def roll(self):
        #Return a random integer in the proper range
        return random.randrange(1, self.sides + 1)

    
    def getSides(self):
        #Just return the number of sides
        return self.sides
