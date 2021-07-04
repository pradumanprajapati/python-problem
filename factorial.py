#Python Program for factorial of a number
'''x=int(input('enter the number'))
fact=1
while(x>0):
     fact=fact*x
     x=x-1
print('fact number',fact)'''
            #OR
x=int(input('enter the number'))
fact=1
for i in range(1,x):
    if x>0:
        fact=fact*x
        x=x-1
print('fact number x:',fact)
