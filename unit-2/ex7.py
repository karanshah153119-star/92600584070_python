list1 = [1, 2, 3, 4, 5, 6, 7]
disc1 = {
    101: 10000,
    102: 20000,
    103: 30000
}

# 1. List Comprehension (Correct)
newList = [x * 2 for x in list1]

# 2. Dictionary Comprehension (Fixed Syntax & Method Name)
newDisc = {k: v * 0.50 for k, v in disc1.items()}

# 3. Set Comprehension (Added to complete your goal)
newSet = {x for x in list1 if x % 2 == 0}

print("List Comprehension:", newList)
print("Dictionary Comprehension:", newDisc)
print("Set Comprehension:", newSet)
