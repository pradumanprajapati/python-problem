'''
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
'''
n=7
for i in range(0,n):
    for j in range(0,n-i-1):
        print("",end=" ")
    for k in range(0,1+i):
        print('*',end=" ")
    print( )