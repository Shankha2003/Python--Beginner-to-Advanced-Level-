print("Calculate the Tip")

bill = int(input("Write your Bill Amount : "))
#print(f"Your Bill amount is : {bill}")

people = int(input("How many people you are : "))

tip = int(input("hpw much Tip do you want to Add (in Rupees) : "))

print(f"Each person Will give : {(bill + tip)/people}")