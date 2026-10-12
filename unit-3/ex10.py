''' 10.Write a program to extract specific information 
from a text file using regular expressions. '''

import re

text = "My ID is 001 and your ID is 002"
ids = re.findall(r"\d+", text)
print(ids)


''' OUTPUT :
        ['001', '002']
'''