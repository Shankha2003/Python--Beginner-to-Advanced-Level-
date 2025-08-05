print("Welcome to Python Pizza Deliveries!\n")

print("Price of Pizza \n" \
"Small pizza(S): Rs. 100 \n" \
"Medium Pizza(M): Rs. 250 \n" \
"Large Pizza(L): Rs. 350 \n" \
"Pepperoni = Rs. 30 \n" \
"Extra Cheese = Rs. 45 \n")

size = str(input("Size of the Pizza : "))
pepperoni = input("Do you want to pepperoni ? Y/N")
extra_cheese =  input("Do you want to add extra cheese ? Y/N")\

bill = 0
if size == "S":
    bill += 100
elif size == "M":
    bill += 250
elif size == "L":
    bill += 350
else :
    print("Wrong Choice!")

if pepperoni == "Y":
    bill += 30
if extra_cheese == "Y":
        bill += 45

print(f"Your final bill is : Rs {bill} . ")