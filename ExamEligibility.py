total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

present_days = total_days - absent_days
percentage = (present_days / total_days) * 100

if percentage >= 75:
    print("The student is allowed to sit for the exam.")
else:
    print("The student is not allowed to sit for the exam.")