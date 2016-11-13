#Filename:   bouns.py
#Written by: Dave Van
#Date:       5/10/10

import die

def main():

    #temp
    total = 0

    #get how many times the user wants to roll a dice
    num_die = input("How many dice to you want to roll? ")

    #get the number of sides of each dice
    side    = input("How many sides does each dice have? ")

    #makes the dice with the sides the user chose
    dice = die.Die(side)

    #roll the dice as many times as the user chose
    for i in range(0, num_die):

        #sums up what each dice rolled
        total += dice.roll()

    #prints the total
    print total

main()
