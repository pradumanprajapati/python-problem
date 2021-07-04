# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

# Age	             Sex	            Wage/day
# >=18 and <30	     M	                 700
#                    F                   750
# >=30 and <=40	     M	                 800
#                    F	                 850
age=int(input("Enter your age\n:"))
sex=input("Enter sex(M/F)\n: ")
wd = int(input("Enter number of days\n:"))
if age>18 and age<30 and sex.upper()=='m':
   total=wd*700
   print("Total wages is \n: ", total)
elif  age > 18 and age < 30 and sex.upper() == 'F':
    total = wd * 750
    print("Total wages is \n: ", total)
elif age>=30 and age<=40 and sex.upper()=='m':
    total = wd * 800
    print("Total wages is \n: ", total)
elif age >= 30 and age <= 40 and sex.upper() == 'F':
    total=wd*850
    print("Total wages is \n: ", total)
else:
    print("Enter appropriate age\n:",age)

