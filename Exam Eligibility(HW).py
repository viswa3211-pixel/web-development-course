from datetime import datetime

# Taking user input
name = input("Enter your name: ")
attendance = float(input("Enter your attendance percentage: "))

# Set exam date (YYYY, MM, DD)
exam_date = datetime(2026, 3, 15)
print("Time now at greenwich meridian is:",end=" ")
print(datetime.now())
print("Exam date is:", end=" ")
print(exam_date)

# Get current date
today = datetime.now()

print("\nChecking exam eligibility...\n")

# Conditional statements
if attendance >= 75:
    if today <= exam_date:
        print("Hello", name + "!")
        print("You are eligible to write the exam.")
        print("All the best!")
    else:
        print("Sorry", name + "!")
        print("The exam date has already passed.")
else:
    print("Sorry", name + "!")
    print("You are not eligible due to low attendance.")