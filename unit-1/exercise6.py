# Program 6: Tuples and Sets Operations

 
print("--- Tuple Operations ---")
point = (10, 25, 50)
fruits_tuple = ("apple", "banana", "cherry", "apple")

print("Tuple:", fruits_tuple)
print("Count of 'apple':", fruits_tuple.count("apple"))
print("Index of 'banana':", fruits_tuple.index("banana"))
 
x, y, z = point
print(f"Unpacked Point coordinates: x={x}, y={y}, z={z}")


 
print("\n--- Set Operations ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
 
print("\nUnion (A | B)        :", set_a.union(set_b))
print("Intersection (A & B) :", set_a.intersection(set_b))
print("Difference (A - B)   :", set_a.difference(set_b))
print("Symmetric Diff (A ^ B):", set_a.symmetric_difference(set_b))

 
set_a.add(10)
set_a.discard(2)   
print("\nSet A after adding 10 and removing 2:", set_a)
 
small_set = {1, 3}
print(f"{small_set} is subset of Set A?", small_set.issubset(set_a))