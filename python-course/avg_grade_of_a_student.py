grade1 = float (input("Type the grade of first test: "))
grade2 = float (input("Type the grade of second test: "))
absences = int (input("Type the number of absences: "))
total_classes = int(input("Type the number of total classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade, 2))
print("Attendance rate: ", str(round((attendance * 100),2)) +'%')

if (avg_grade >= 6 and attendance >= 0.8 ):
    print ("The student has been approved")
elif (avg_grade < 6 and attendance < 0.8):
    print ("The student has failed due to an average grade lower than 6.0 and attendance rate lower than 80%")
elif (attendance >= 0.8):
  print ("The student has failed due to an average grade lower than 6.0.")
else:
  print("The student has failed due to an attendance rate lower than 80%")