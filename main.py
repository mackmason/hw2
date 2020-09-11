# Author: Mack Mason mjm8542@psu.edu

def getGradePoint(grade):
  if (grade == "A"):
    return 4.0
  elif (grade == "A-"):
    return 3.67
  elif (grade == "B+"):
    return 3.33
  elif (grade == "B"):
    return 3.0
  elif (grade == "B-"):
    return 2.67
  elif (grade == "C+"):
    return 2.33
  elif (grade == "C"):
    return 2.0
  elif (grade == "D"):
    return 1.0
  else:
    return 0.0
 
courseOneLetterGrade = input("Enter your course 1 letter grade: ")   
courseOneCredit = float(input("Enter your course 1 credit: "))
courseOneGradePoint = getGradePoint(courseOneLetterGrade)
print(f"Grade point for course 1 is: {courseOneGradePoint}")  

courseTwoLetterGrade = input("Enter your course 1 letter grade: ")  
courseTwoCredit = float(input("Enter your course 1 credit: "))
courseTwoGradePoint = getGradePoint(courseTwoLetterGrade)
print(f"Grade point for course 1 is: {courseTwoGradePoint}")  

courseThreeLetterGrade = input("Enter your course 1 letter grade: ")
courseThreeCredit = float(input("Enter your course 1 credit: ")) 
courseThreeGradePoint = getGradePoint(courseThreeLetterGrade)
print(f"Grade point for course 1 is: {courseThreeGradePoint}")  

GPA = (courseOneGradePoint * courseOneCredit + courseTwoGradePoint * courseTwoCredit + courseThreeGradePoint * courseThreeCredit) / (courseOneCredit + courseTwoCredit + courseThreeCredit)
print(f"Your GPA is: {GPA}")