# Write a program to iterate over lists strings and
# dictionaries using loops.
list1 = ["dog","cat","frog","lion","eagle"]
disc = {
    "name":"karan",
    "id":1221,
    "address":"rajkot",
    "country":"india"
}

for l in list1:
    print(l)
    
for key,value in disc.items():
    print(f"{key} -> {value}") 