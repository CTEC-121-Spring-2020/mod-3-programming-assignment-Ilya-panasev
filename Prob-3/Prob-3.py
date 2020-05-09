# Module 3
#   Programming Assignment 4
#     Prob-3.py

"""
Input: a number between 0-5
Processes: converts the number into a letter grade. 
Unit testing prints out the letterGrade function in order to test the conversion.
Output: a letter grade/score
"""
# Ilya Panasevich

def letterGrade(score):

    if score == 2:
        grade = "D"

    elif score == 3:
        grade = "C"
    
    elif score == 4:
        grade = "B"

    elif score == 5:
        grade = "A"
    
    else:
        grade = "F"

    return grade

def unitTest():
    print("If your grade score is 0 your letter score is:", letterGrade(0), "\n")
    print("If your grade score is 1 your letter score is:", letterGrade(1), "\n")
    print("If your grade score is 2 your letter score is:", letterGrade(2), "\n")
    print("If your grade score is 3 your letter score is:", letterGrade(3), "\n")
    print("If your grade score is 4 your letter score is:", letterGrade(4), "\n")
    print("If your grade score is 5 your letter score is:", letterGrade(5), "\n")

if __name__ == "__main__":
    unitTest()
