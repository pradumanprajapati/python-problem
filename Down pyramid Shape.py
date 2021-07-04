'''
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
'''
n=6
for i in range(0,n):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(2*n,2*i+1,-1):
        print("*",end=" ")

    print()

# n=int(input("enter the number\n"))
#
# for i in range(0,n):
#     for j in range(0,i):
#          print(" ",end=" ")
#     for k in range(2*n,2*i+1,-1):
#            print("*",end=" ")
#
#     print()