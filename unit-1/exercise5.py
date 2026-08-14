# Program 5: List Creation, Indexing, Slicing, and List Comprehensions

 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", numbers)

 
print("\n--- Indexing ---")
print("First element (index 0)   :", numbers[0])
print("Last element (index -1)   :", numbers[-1])
print("Fifth element (index 4)   :", numbers[4])
 
print("\n--- Slicing ---")
print("First 4 elements (0:4)    :", numbers[:4])
print("Elements from index 3 to 7:", numbers[3:8])
print("Every second element (::2):", numbers[::2])
print("Reversed list (::-1)      :", numbers[::-1])
 
print("\n--- List Comprehensions ---")
 
squares = [x**2 for x in range(1, 11)]
print("Squares (1-10):", squares)

 
even_doubled = [x * 2 for x in numbers if x % 20 == 0]
print("Multiples of 20 doubled:", even_doubled)

 
fruits = ["apple", "banana", "cherry", "date"]
first_letters = [fruit[0].upper() for fruit in fruits]
print("First letters uppercase:", first_letters)