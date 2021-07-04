# Accept the electric units from user and calculate the bill according to the following rates.
# First 100 Units     :  Free
# Next 200 Units      :  Rs 2 per day.
# Above 300 Units    :  Rs 5 per day.
# if number of unit is 500 then total bill = 0 +400 + 1000 = 1400

amount = int(input("Enter number of units"))
if amount <=100:
     total = 0
elif amount >100 and amount <= 300:
     total = (amount-100)*2
else:
    total = 400 + (amount - 300)*5# it is the 500 of target of base of the total bill amount
print("Total amount to pay is ", total)

