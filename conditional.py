# This program assigns grades based on the marks entered by the user.
marks = int(input("Enter your marks: "))
if(marks>=80 and marks<=100):
    print("Grade A")
elif(marks>=60 and marks<80):
    print("Grade B")
elif(marks>=40 and marks<60):
    print("Grade C")
elif(marks>= 0 and marks<40):
    print("Grade F")
else:
    print("Invalid Marks Entered.")