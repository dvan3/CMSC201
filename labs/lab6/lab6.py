#Filename:   lab6.py
#Written by: Dave Van
#Date:       3/22/10

NUM_SCORES = 13
LAB_DIVISOR = 30.0

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

    infile = open("grades.txt", "r")

    grades_file = open("grade_report.txt", "w")

    class_grades = []

    for line in infile:
        data = line.split()

        name = data[0]

        scoreStrings = data[1:]

        scores_list = [float(x) for x in scoreStrings]

        score = findCourseScore(scores_list)

        Letter_grade = findLetterGrade(score)

        class_grades.append(score)

        grades_file.write("%12s: %6.2f - %s\n" % ( name, score, Letter_grade))

    infile.close()

    average = sum(class_grades)/ len(class_grades)

    grades_file.write("\n    Class average: %.2f\n" % (average))

    grades_file.close()
    
main()


    

    
