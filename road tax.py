#Write a program to accept the cost price of a bike and display the  to be paid according to the following criteria :
# Cost price (in Rs)                             Tax
# > 100000                                       15 %
# > 50000 and <= 100000                          10%
# <= 50000                                        5%

amount=int(input('enter the road tax amount'))
tax=0
n=100
if amount>=10000:
    tax=15/n*amount
elif amount>=5000 and amount<=10000:
    tax=10/n*amount
elif amount<=5000:
    tax=5/n*amount
print('created amount',amount)
print('Road tax',tax)


