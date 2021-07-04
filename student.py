'''#Accept the percentage from the user and display the  grade according to the following criteria:
#    Below 25 —- D
#    25 to 45 —- C
#    45 to 50 —- B
#    50 to 60 –– B+
#    60 to 80 — A
#    Above 80 –- A+

n=int(input('enter the student number'))
if n<=25:
    print('That is the student of number 25 is less then of grade:\n', 'D',n)
elif n<=25 and n>=45:
    print('That is the student of number 45 is grater then of grade:\n', 'C', n)
elif n<=45 and n>=50:
    print('That is the student of number 50 is less then of grade:\n', 'B', n)
elif n<=50 and n>=60:
    print('That is the student of number 60 is grater then of grade:\n', 'B+', n)
elif n>=60 and n<=80:
    print('That is the student of number 80 is less then of grade:\n', 'A', n)
elif n>=80:
    print('That is the student of number 80 Above then of grade:\n', 'A+', n)'''''


# Write a program to accept percentage and display the Category according to the  following criteria :
# Percentage	          Category
# < 40                    	Failed
# >=40 & <55	            Fair
# >=55 & <65	            Good
# >=65	                    Excellent

num=int(input('enter the number of student\n'))
if num<=40:
    print('student  40 less then failed:\n')
elif num>=40 and num<=55:
    print('student  55 less then fair:\n')
elif num>=55 and num<65:
    print('student  65 less then Good:\n')
elif num>=65:
 print('student  55 less then Excellent:\n')
