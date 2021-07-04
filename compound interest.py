x=int(input('enter the principal balance\n'))
t=int(input('enter the 	time periods \n'))
r=int(input('enter the interest rate\n'))
ci=x*(pow((1 +r/100),t))
a=ci-x #compaund interest - principal amount
print('total interest of compaunad \n a:',a)