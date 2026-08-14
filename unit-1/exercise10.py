# Program 10: Demonstrating Recursion using Factorial and Fibonacci Series

 
def factorial(n):
 
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:  # Base case
        return 1
    else:                   # Recursive step
        return n * factorial(n - 1)


 
def fibonacci(n):
 
    if n < 0:
        return "Invalid input"
    elif n == 0:            # Base case 1
        return 0
    elif n == 1:            # Base case 2
        return 1
    else:                   # Recursive step
        return fibonacci(n - 1) + fibonacci(n - 2)


 
if __name__ == "__main__":
    
 
    print("=== 1. Factorial Demonstration ===")
    num = 5
    result = factorial(num)
    print(f"Factorial of {num} ({num}!): {result}")
    
 

    print("\n" + "=" * 40 + "\n")
 
    print("=== 2. Fibonacci Series Demonstration ===")
    terms = 8
    print(f"First {terms} terms of the Fibonacci series:")
    
    fib_series = [fibonacci(i) for i in range(terms)]
    print("Series:", " -> ".join(map(str, fib_series)))