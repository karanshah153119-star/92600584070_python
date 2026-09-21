# Write a program to check whether a number is
# positive negative or zero using nested
# conditions

num = int(input("enter your number "))

if(num != 0):
    if(num>0):
        print("number is positive")
    else:
        print("number is negative")
else:
    print("number is zero")