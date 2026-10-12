''' 9. Write a program to use re module functions 
such as match search and findall. '''

import re

text = "Python is amazing and Python is fast"

match_result = re.match(r"Python", text)
print(match_result.group())

search_result = re.search(r"amazing", text)
print(search_result.group())

findall_result = re.findall(r"Python", text)
print(findall_result)


''' OUTPUT :
        Python
        amazing
        ['Python', 'Python']
'''