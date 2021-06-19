#import os
#import pdb
print("This is the birthday Dictionary We know the birthdays of:")
print("Salman Khan")
print("Shah Rukh Khan")
print("Ajay Devgan")
print("Which persons birthday do you want")
Actor = input()
if Actor=='Salman Khan':
    print("December 27, 1965")

elif Actor=='Shah Rukh Khan':
    print("November 2,1965")
elif Actor=='Ajay Devgan':
    print("April 2, 1969")

else:
    print("Restart Program")