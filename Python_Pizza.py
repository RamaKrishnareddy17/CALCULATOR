print(" Welcome to Python Pizza Deliveres? ")

small_size = 's'
Medium_size ='m'
large_size = 'l'

size = input(" What size do you want? S, M, L : ")
pepperoni = input("Do you want to pepperoni on your pizza? y or n : ")
extra_cheese = input("Do you want extra cheese? y or n : ")

bill = 0
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("wrong inputs!!")

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"your final bill is : ${bill}.")