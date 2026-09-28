# Write a program to generate a sequence of
# numbers using generator functions and yield
# keyword.
# A generator function uses 'yield' instead of 'return'
def sequence_generator(start, end, step=1):
    current = start
    while current <= end:
        yield current  # Suspends function, returns value, and saves state
        current += step

# 1. Using the generator in a loop
print("Generated Sequence:")
for num in sequence_generator(5, 25, 5):
    print(num, end=" ")  # Output: 5 10 15 20 25
print("\n")

# 2. Controlling the generator manually
gen = sequence_generator(1, 3)
print("Manual Fetching:")
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen)) # Triggers StopIteration automatically
