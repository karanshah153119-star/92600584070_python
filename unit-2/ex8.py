# 1. Global Variable
# This variable is defined at the topmost level of the script.
# It can be read anywhere, but needs the 'global' keyword to be modified inside a function.
message = "I am Global"

def outer_function():
    # 2. Enclosing (Nonlocal) Variable
    # This variable belongs to the outer function. 
    # It is "local" to outer_function, but "nonlocal" to inner_function.
    message = "I am Enclosing (Nonlocal)"
    
    def inner_function():
        # 3. Local Variable
        # This variable is completely private to inner_function.
        message = "I am Local"
        print("Inside inner_function (Local):", message)
        
    def modify_nonlocal():
        # Using the 'nonlocal' keyword allows us to modify the variable 
        # in the nearest enclosing (outer) scope.
        nonlocal message
        message = "I have been modified by inner function!"
        
    # Run the inner functions to see the scope rules in action
    print("\n--- Before any modifications ---")
    inner_function()
    print("Inside outer_function:", message)
    
    print("\n--- Modifying the Enclosing variable ---")
    modify_nonlocal()
    print("Inside outer_function after nonlocal change:", message)


def modify_global():
    # Using the 'global' keyword binds this variable to the top-level global variable.
    global message
    message = "Global has been changed!"


# --- Execution Flow ---
print("Initial Global message:", message)

# Call the outer function to see local vs nonlocal behavior
outer_function()

# Modify the global variable
print("\n--- Modifying the Global variable ---")
modify_global()
print("Final Global message:", message)
