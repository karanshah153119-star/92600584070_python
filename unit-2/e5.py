# Write a program to demonstrate the use of
# break continue and pass statements

for i in range(1,11):
    if(i==8):
        print("program stopped at 8")
        break
    if(i%2==0):
        continue
    if(i==8):
        break
    if(i==5):
        pass
    print(i)