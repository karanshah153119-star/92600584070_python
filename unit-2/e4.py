# Write a program to find the sum of digits of a
# number using a while loop.
num = int(input("enter your number "))
x = num
sum = 0
while x>0:
    sum=sum+(x%10)
    x = x//10
print(sum)