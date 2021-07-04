# Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:
# Marked Price	        Discount
# >10000	             20%
# >7000 and <=10000	      15%
# <=7000	              10%

price=int(input('enter the market price\n'))
discount=0
total=0
if price>=10000:
      discount=price*20/100
elif price>=7000 and price<=10000:
     discount=price*15/100
elif price<=7000:
     discount=price * 10 / 100
total=price-discount
print('Net amount ',total)
