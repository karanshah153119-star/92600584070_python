# Program 4: String Operations

text = "   Hello, Python Programming World!   "

 
clean_text = text.strip()  # Removing leading/trailing whitespace first
print("--- String Slicing ---")
print(f"Original Text : '{clean_text}'")
print(f"First 5 chars (0:5)   : '{clean_text[:5]}'")
print(f"Substring (7:13)      : '{clean_text[7:13]}'")
print(f"Last 6 chars (-6:)    : '{clean_text[-6:]}'")
print(f"Reversed String (::-1): '{clean_text[::-1]}'")
print(f"Every 2nd char (::2)  : '{clean_text[::2]}'")

 
print("\n--- String Formatting ---")
name = "Dev"
score = 94.5678

 
print(f"f-string   : Student {name} scored {score:.2f}%")

 
print("str.format : Student {} scored {:.1f}%".format(name, score))
 
print("%% operator : Student %s scored %.2f%%" % (name, score))

 
print("\n--- Built-in String Methods ---")
raw_msg = "python programming is versatile"

print(f"Uppercase       : '{raw_msg.upper()}'")
print(f"Title Case      : '{raw_msg.title()}'")
print(f"Replace Word    : '{raw_msg.replace('python', 'Java')}'")
print(f"Find Index      : 'programming' starts at index {raw_msg.find('programming')}")

 
words = raw_msg.split()
print(f"Split to List   : {words}")

joined_str = "-".join(words)
print(f"Joined with '-' : '{joined_str}'")