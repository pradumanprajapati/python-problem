num = int(input())
total= 0
t=str(num)
for i in  range(len(t)):
    total = total+(int(t[i])**len(t))
# print(total)
if total == num:
    print('arms')
else:
    print('not arms')