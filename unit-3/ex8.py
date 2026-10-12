''' 8. Write a program to demonstrate basic regular 
expression pattern matching. '''

import re

text = "Call me at 123-456-7890 or 987-654-3210"
phone_pattern = r"\d{3}-\d{3}-\d{4}"

first_match = re.search(phone_pattern, text)
print(first_match.group())

all_matches = re.findall(phone_pattern, text)
print(all_matches)

censored_text = re.sub(phone_pattern, "XXX-XXX-XXXX", text)
print(censored_text)


''' OUTPUT :
        123-456-7890
        ['123-456-7890', '987-654-3210']
        Call me at XXX-XXX-XXXX or XXX-XXX-XXXX
'''