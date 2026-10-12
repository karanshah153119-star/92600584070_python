''' 2. Write a program to demonstrate different 
import mechanisms in Python. '''

import module2 

a = 10 
b = 20 

ans = module2.add(a,b)
print("Answer Mechnism1 : ",ans)


from module2 import sub

a = 20
b = 10

ans = sub(a,b)
print("Answer Mechnism2 : ",ans)


from module2 import sub as subtract

a = 40
b = 20

ans = subtract(a,b)
print("Answer Mechnism3 : ",ans)


from module2 import *

a = 60
b = 20

ans = add(a,b) , sub(a,b)
print("Answer Mechnism2 : ",ans)


''' OUPUT :
        Answer Mechnism1 :  30      
        Answer Mechnism2 :  10      
        Answer Mechnism3 :  20      
        Answer Mechnism2 :  (80, 40)
'''