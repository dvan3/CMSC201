#Filename:   lab10.py
#Written by: Dave Van
#Date:       4/19/10

def printGreeting():
    print "\nThis program will give you the min, max, average, median, and"
    print "and the st. dev by using a dictionary\n"

def readFile(filename):
    file = open(filename)

    grades = {}
    
    for line in file:
        (name, gradeStr) = line.strip().split()

        grades[name] = float(gradeStr)

    return grades

def findMean(scores):
    return sum(scores) / len(scores)

def findMedian(scores):
    i = len(scores)
    if not i % 2:
        return (scores[(i / 2) - 1] + scores[i / 2]) / 2.0
    return scores[i / 2]

def main():
    printGreeting()

    filename = raw_input("Enter a filename: \n")

    #scores is a dictionary
    scores = readFile(filename)

    scoreValues = scores.values()

    scoreValues.sort()

    minimum = min(scoreValues)
    maximum = max(scoreValues)
    mean = findMean(scoreValues)
    median = findMedian(scoreValues)

    print "Minimum = ", minimum
    print "Maximum = ", maximum
    print "Mean    = ", mean
    print "Median  = ", median

main()
