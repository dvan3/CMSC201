#File name: lab5.py
#Author:    Dave Van
#Date:      3/8/10

NUM_SCORES = 13
LAB_DIVISOR = 30.0

#Prints Greeting
def greeting():
    
    print "This program will compute the weighted final grade for a 201 student\n"

#Finds the course score
def findCourseScore(courseDataList):
    
    total_score = 0.0
    
    for i in range(NUM_SCORES):
        weight = courseDataList[i * 2]
        score  = courseDataList[i * 2 + 1]

        weighted_score = weight * score

        if weight == .1:
            weighted_score = findLabScore(weighted_score)

        total_score += weighted_score

    return total_score

#Finds the lab score
def findLabScore(LabScore):
    
    return (LabScore / LAB_DIVISOR) * 100

#Prints the letter grade
def findLetterGrade(courseScore):
    
    if courseScore < 60:
        return "F"
    if courseScore < 70:
        return "D"
    if courseScore < 80:
        return "C"
    if courseScore < 90:
        return "B"
    else:
        return "A"

    
def main():
    greeting()
    name = raw_input()

    scores_list = []

    for i in range(NUM_SCORES * 2):
        score = input()
        scores_list.append(score)

    score = findCourseScore(scores_list)

    Letter_grade = findLetterGrade(score)

    print "%s: %.2f - %s" % ( name, score, Letter_grade)


main()






