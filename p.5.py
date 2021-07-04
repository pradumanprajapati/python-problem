'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n=int(input('enter the number\n'))
for i in range(0,n):
    for j in range(i):
        print('*',end=" ")
    print( )
for i in range(n+1):
    for j in range(n-i,0,-1):
        print('*',end=" ")
    print( )