# Program 9: User-Defined Functions and Argument Types

 
def greet_user(name, greeting="Hello", punctuation="!"):
    """Demonstrates positional & default parameters."""
    return f"{greeting}, {name}{punctuation}"

def calculate_summary(title, *scores, **metadata):
    """
    title    : Positional arg
    *scores  : Gathers extra positional arguments into a tuple
    **metadata: Gathers extra keyword arguments into a dictionary
    """
    total = sum(scores)
    avg = total / len(scores) if scores else 0
    
    print(f"--- {title} ---")
    print(f"Scores Tuple (*args)    : {scores}")
    print(f"Total: {total}, Average: {avg:.2f}")
    
    print("Metadata Dict (**kwargs):")
    for key, value in metadata.items():
        print(f"  - {key}: {value}")
 
msg1 = greet_user("Alice")
print(msg1)
 
msg2 = greet_user(greeting="Welcome", name="Bob", punctuation="!!!")
print(msg2)

print()
 
calculate_summary(
    "Exam Report",
    85, 90, 78, 92, 88,            # *args (scores)
    student="Charlie", term="Fall", year=2026  # **kwargs (metadata)
)