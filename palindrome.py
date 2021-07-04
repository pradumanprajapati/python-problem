num=int(input('enter the armstrong number'))
sum=0
rev =0
str=num
while num!=0:
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
if num == rev:
    print('palindrome')
else:
    print('not palindro e')
