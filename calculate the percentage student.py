#  Accept the following from the user and calculate the percentage of class attended:
# a.     Total number of working days
# b.     Total number of days for absent
# After calculating percentage show that, If the percentage is less than 75,
# than student will not be able to sit in exam.

m=int(input('enter the total day attended:\n'))
n=int(input('enter the weeks absent:\n'))
c=m-n
print('total attended of the student-Absent student\n',c)
v=c*m/100
if v<=75:
    print('student will be not apper exam\n',v)
else:
    print('studenth will be apper exam\n',v)

