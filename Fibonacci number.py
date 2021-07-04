#Python Program for n-th Fibonacci number

'''x=int(input('enter the fibonacci number x:'))
n1=0
n2=1
count=0
if x<=0:# x is the greater then of 0 that print positive number
    print('positive number',x)
elif x==1: # x==1 that is the fibonacci sequnce that are the n1=0 se start
    print('fibonacci sequnce up to ',x)
    print(n1)
else:
    print('fibnacci sequnce of number',x)
    while count<=x: # loop of the count  greater then equltu  x
        print(n1) # n1=0 is print
        b1=n1+n2 #  the n1 and n2 of add that store b1 is variable
        n1=n2
        n2=b1
        count+=1'''


# Python Program for How to check if a given number is Fibonacci number?

import math
# mathematical functions define
def Square(x):
    # the function that returns true if x is square
    num = int(math.sqrt(x))
    return num * num==x
    # Returns true if n is a Fibinacci Number, else false
def Fibonacci(num):
    return Square(5 * num * num + 4)
    # one varibal of the n square and anddition(5*n*n+4)
for i in range(1, 11):
    #useing of for loop
    if (Fibonacci(i) == True):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is a not Fibonacci Number ")

