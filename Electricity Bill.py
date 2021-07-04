# Write a program to calculate the electricity bill (accept number of unit from user),
# according to the following criteria :
#    Unit                                                     Price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill m is Rs2000)

m=int(input('enter the number'))
amount=0
if m<=100:
    amount =0
elif m<=100 and m>=200:
   amount=(m-100)*5
elif m>=200 :
    amount= 500+(m - 200) * 10
    print('totla amount ',amount)