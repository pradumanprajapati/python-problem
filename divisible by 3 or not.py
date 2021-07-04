#Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.+/p
n=int(input('enter the digit'))
v=n%10
if v%3==0:
    print('divisibalr value',v)
else:
    print('not divisiale value',v)