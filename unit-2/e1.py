# Write a program to demonstrate conditional
# statements using if if-else and if-elif-else.

# Apply your knowledge of Python conditional statements by writing a program for a shopping bill system. Accept the total purchase amount from the user and use if, if-else, and if-elif-else statements to check discount eligibility and display the appropriate discount category.

amount = int(input("enter purchased amount "))
discount = 0
if(amount<0):
    print("please enter valid amount")
    
if(amount>1000):
    print("you are eligable for discount")
    if(amount>1000 or amount<2500):
        discount = 10
    elif(amount>2500  or amount<3500):
        discount = 20
    elif(amount>3500  or amount<4500):
        discount = 30
    elif(amount>4500  or amount<5500):
     discount = 40
    elif(amount>5500):
        discount = 50
    print(f"disount : {discount}%")
else:
    print("you are not eligable for discount")

print(f"final amount : {amount-amount*(discount/100)}")
