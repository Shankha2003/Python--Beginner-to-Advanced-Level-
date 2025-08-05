print("Welcome to the Rollercoaster ! ")
height = int(input("Enter your Height here( in cm )"))
bill = 0

if height >= 130 :
    print("You can Ride")
    age = int(input("Enter you Age : "))
    if age <= 12:
        bill = 100
        print("Pay rs. 100")
    elif age <= 18 :
        bill = 150
        print("Pay rs. 150")
    elif age >= 45 and age <= 55 :
        bill = 0
        print("Have a free ride on us !")
    else:
        bill = 200
        print("Pay rs. 200")


    pic = input("Do you want a Photo ? ")
    if pic == "y":
        bill += 30
    print(f"Your Final bill is {bill} . ")
        
else :
    print("You can't Ride . ")
