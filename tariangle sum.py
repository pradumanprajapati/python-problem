# Accept three sides of triangle and check whether the triangle is possible or not.
# (triangle is possible only when sum of any two sides is greater than 3rd side)
t1=int(input('enter the first triangle of sides:\n'))
t2=int(input('enter the secound triangle of sides:\n'))
t3=int(input('enter the third triangle of sides:\n'))
v=t1+t2
b=t2+t3
g=t1+t3
if v>=t3 and b>=t1 and g>=t2:
    print('triangle is possible:\n')
else:
    print('not triangle is possible\n')