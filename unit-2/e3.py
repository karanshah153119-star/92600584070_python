# Write a program to generate a multiplication
# table using a for loop.
# Program to generate multiplication table using a for loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
