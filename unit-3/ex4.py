''' 4. Write a program to generate random numbers 
using random module. '''

import random

print("Random float between 0 and 1:",random.random())
print("Random Dice Rolled? : ",random.randint(1,6))
print("Random Even Numbers between 1 to 20:",random.randrange(1,20,2))


''' OUTPUT : 
        Random float between 0 and 1: 0.8987086278984228
        Random Dice Rolled? :  5
        Random Even Numbers between 1 to 20: 19
'''