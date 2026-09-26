print("welcome to my course")


Student_name = str(input("what's your name? "))
Student_age = int(input("how old are you? "))
Major = str(input("what's your Major? "))
credit_hours = int(input("how many credit hours? "))
Price_credit_hours = int(input("how many price credit hours? "))
Number_of_courses = int(input("how many courses? "))


Total_cost = credit_hours * Price_credit_hours
Average_hours_per_course = credit_hours / Number_of_courses
age_after4 = Student_age + 4

print("\n    University Registration    \n",
      "\nstudent name :",Student_name,
      "\nAge :",Student_age,
      "\nMajor :",Major,
      "\nCredit hours :",credit_hours,
      "\nprice credit hours :",Price_credit_hours,
      "\nNumber of courses :",Number_of_courses,
      "\n\n--------- Registration Info ---------\n",
      
      "\nTotal cost :",Total_cost,
      "\nAverage hours per course :",Average_hours_per_course,
      "\nExpected age after graduation",age_after4,
      "\n\n      Registration Complete       ")

input()