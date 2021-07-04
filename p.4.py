# write the progarm of the accept of the user in the patten in the python
'''
0
0 1
0 1 2
0 1 2 3
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
 '''

n=int(input('enter the number\n'))
k=int(input('enter the number\n'))
for i in range(0,n):
    for j in range(i):
        print(j,end=" ")
    print( )
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print( )