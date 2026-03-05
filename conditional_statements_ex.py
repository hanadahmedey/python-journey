# Write a program to generate remarks for awarding middle school children. Use your own remarks based on 4 subjects
# Allow the users to enter individual subject marks. The marks should be in pure integer form
# The grading is being provided as per the total marks
# Find (total marks, average)
English = int(input("Enter your marks"))
Mathematics = int(input("Enter your marks"))
Science = int(input("Enter your marks"))
Social_studies = int(input("Enter your marks"))
Total_marks = English + Mathematics + Science + Social_studies
Average = Total_marks/4
print("The total marks is:",Total_marks)
print("The average is:",Average)
if Average>=90:
    print("Excellent")
elif Average>=75:
    print("Great")
elif Average>=60:
    print("Good")
elif Average>=45:
    print("Pass")
else:
    print("Repeat")
                    
