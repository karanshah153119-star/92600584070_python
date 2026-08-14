# Program 8: Explaining Mutable vs Immutable Objects

print("=== 1. IMMUTABLE OBJECTS (Integers, Strings, Tuples) ===")
 
x = 100
print(f"Initial x = {x}, Memory ID: {id(x)}")

x = x + 1  
print(f"Updated x = {x}, Memory ID: {id(x)}  <-- ID changed!")

text = "Hello"
print(f"\nInitial text = '{text}', Memory ID: {id(text)}")
text += " World"
print(f"Updated text = '{text}', Memory ID: {id(text)} <-- ID changed!")

 
 


print("\n=== 2. MUTABLE OBJECTS (Lists, Dictionaries, Sets) ===")
 

my_list = [1, 2, 3]
print(f"Initial list = {my_list}, Memory ID: {id(my_list)}")

my_list.append(4)
my_list[0] = 99
print(f"Modified list= {my_list}, Memory ID: {id(my_list)} <-- ID remains SAME!")
 
alias_list = my_list
alias_list.append(500)
print("\nAdded 500 to 'alias_list':")
print(f"my_list is now   : {my_list}")
print(f"alias_list is now: {alias_list}")