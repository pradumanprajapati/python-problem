num = int(input("Enter any number: "))
for i in range(2, num):
    if (num % i) == 0:
        print('this is not prime number ',num)
        break
else:
        print("this is prime number :",num)