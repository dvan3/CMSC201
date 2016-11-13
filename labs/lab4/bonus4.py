#header here

def main():

    SMOKE_VOTE = 18
    DRINK = 21
    RENT = 25
    SENATOR = 30
    CITIZEN_SEN = 9
    PRESIDENT = 35
    LIVING_USA = 14
    BORN_IN_USA = 1
    
    age = input("Enter your age: ")
    citizen = input("How many years have you been a U.S. Citizen? ")
    born = input("Were you born in the U.S.A.(0 if NO, 1 if YES): ")
    living = input("How long have you been living in the U.S.? ")
    felony = input("How many times have you been convicted a felony? ")

    if age >= SMOKE_VOTE:
        print "You CAN smoke"
    else:
        print "You CANNOT smoke"

    if age >= DRINK:
        print "You CAN drink"
    else:
        print "You CANNOT drink"

    if age >= RENT:
        print "You CAN rent a car in Maryland"
    else:
        print "You CANNOT rent a car in Maryland"

    if age >= SMOKE_VOTE and felony < 1:
        print "You CAN vote"
    else:
        print "You CANNOT vote"

    if age >= SENATOR and citizen >= CITIZEN_SEN:
        print "You CAN be a US Senator, but why would you?"
    else:
        print "You CANNOT be a US senator and keep it that way"

    if age >= PRESIDENT and living >= LIVING_USA and born == BORN_IN_USA:
        print "You CAN be President of the USA and destroy the world"
    else:
        print "You CANNOT be President of the USA"

main()
