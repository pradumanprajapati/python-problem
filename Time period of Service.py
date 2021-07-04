# A company decided to give bonus to employee according to following criteria:
# Time period of Service         Bonus
# More than 10 years             10%
# >=6 and <=10                   8%
# Less than 6 years              5%
# Ask user for their salary and years of service and print the net bonus amount

emp=int(input('enter the emp salary service\n'))
n=int(input('enter the emp time period:\n'))
v=emp*n/100
print('divided time period\n',v)
if v>=10:
    print('company of banus of service 10% year\n',v)
elif v>=6 and v<=10:
    print('company of banus of service 8% year\n',v)
elif v<=6:
    print('company of banus of service 5% year\n',v)