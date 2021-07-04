#Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days  : Rs 3/day.
# Ten to 15 days  : Rs 4/day
# After 15 days    : Rs 5/day
lib=int(input('enter the number of day:\n'))
# day=int(input('enter the day:\n'))
total=0
if lib>=5:
    total =lib* 2
elif lib>=6 and lib<=10:
    total = lib*3
elif lib>=10 and lib<=15:
    total=lib*4
elif lib>=15:
    total= lib*5
print(lib)
print(total)