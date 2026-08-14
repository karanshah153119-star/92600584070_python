# Program 7: Dictionary Creation, Methods, and Iteration

# 1. Creating a dictionary
student = {
    "name": "Alex",
    "age": 20,
    "course": "Computer Science",
    "gpa": 3.8
}

print("Initial Dictionary:\n", student)

# 2. Accessing & Adding/Updating elements
print("\n--- Access & Modification ---")
print("Name (using key) :", student["name"])
print("GPA (using get())  :", student.get("gpa"))
print("Grade (missing key):", student.get("grade", "Not Assigned"))  # Default fallback

# Updating existing key & adding new key
student["gpa"] = 3.9
student["email"] = "alex@example.com"
print("Updated Dictionary:\n", student)

# 3. Dictionary Iteration
print("\n--- Iteration Techniques ---")

print("Keys:")
for key in student.keys():
    print(f" - {key}")

print("\nValues:")
for value in student.values():
    print(f" - {value}")

print("\nKey-Value Pairs (Items):")
for key, value in student.items():
    print(f" {key:<10} : {value}")

# 4. Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print("\nDictionary Comprehension (x: x^2):", squares_dict)