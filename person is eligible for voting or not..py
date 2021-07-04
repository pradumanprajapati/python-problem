#Write a program to check whether a person is eligible for voting or not. (accept age from user)
n=input('enter the name')
m=int(input('enter the age'))
if m>=18:
    print('eligible',m)
else:
    print('not eligible',m)