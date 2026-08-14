# Program 2: Data Types and Type Casting

 
num_int = 42
num_float = 3.14159
text_str = "100"
flag_bool = True
colors_list = ["red", "green", "blue"]

print("--- Data Types ---")
print(f"{num_int} is of type:", type(num_int))
print(f"{num_float} is of type:", type(num_float))
print(f"'{text_str}' is of type:", type(text_str))
print(f"{flag_bool} is of type:", type(flag_bool))
print(f"{colors_list} is of type:", type(colors_list))

 
print("\n--- Type Casting ---")

 
str_to_int = int(text_str)
str_to_float = float(text_str)
print(f"String '{text_str}' -> Int: {str_to_int} (Type: {type(str_to_int).__name__})")
print(f"String '{text_str}' -> Float: {str_to_float} (Type: {type(str_to_float).__name__})")
 
float_to_int = int(num_float)
print(f"Float {num_float} -> Int: {float_to_int} (Type: {type(float_to_int).__name__})")

 
zero_bool = bool(0)
num_bool = bool(5)
print(f"bool(0) is {zero_bool}, while bool(5) is {num_bool}")

 
char_list = list("Python")
print(f"String 'Python' -> List: {char_list}")