#  Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
'''n=int(input('entr the number'))
if n%2==0:
    print('divisibale number:\n',n)
else:
    print('not divisibale number')
if n%3==0:
    print('divisibale number:\n', n)
else:
    print('not divisibale number')'''

#  Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
n = int(input("Enter first number\n"))
if n%2==0 and n%3==0:
      print("Number is divisible by 2 and 3 both:\n",n)
else:
      print("Number is not divisible by both:\n",n)