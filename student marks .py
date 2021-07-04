# Write a program to accept percentage from the user and display the grade according to the following criteria:
# Marks                      Grade
# > 90                         A
# > 80 and <= 90               B
# >= 60 and <= 80              C
# below 60                     D

'''n=int(input('enter the student marks '))
if n>=90:
    print('display the grade =',n,'A')
elif n>=80 and n<=90:
    print('display the grade =',n,'B')
elif n>=60 and n<=80:
    print('display the grade =',n,'C')
elif n<=60 :
    print('display the grade =',n,'D')
'''

# Write a program to accept five subject percentage from the user and display the grade and marks according
'''
M=int(input('enter the student math marks '))
S=int(input('enter the student scince marks '))
E=int(input('enter the student english marks '))
H=int(input('enter the student hindi marks '))
C=int(input('enter the student computer marks '))
total=M+S+E+H+C
n=total*100/500
if n>=90:
    print('display the grade of fast=',n,'A')
elif n>=80 and n<=90:
    print('display the grade of secound =',n,'B')
elif n>=60 and n<=80:
    print('display the grade  of third =',n,'C')
if n<=50:
    print('display the grade of fail =',n,'D')
print('total marks',total)
print('divisibale amount',n)
'''
M,S,E,H,C=map(int,input().split())
total=M+S+E+H+C
print(total)