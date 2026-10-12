''' 5. Write a program to display current date and 
time using datetime module. '''

import datetime

# 1. Current Date and Time of System 
print("Current Date and Time : ",datetime.datetime.now())

# 2. Formated Date and Time
date = datetime.datetime.now()
print("Fromated Date and Time : ",date.strftime("%d-%m-%Y %I:%M:%S %p"))


''' OUTPUT :
        Current Date and Time :  2026-09-28 10:10:17.165880
        Fromated Date and Time :  28-09-2026 10:10:17 AM
'''