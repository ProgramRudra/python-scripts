import random
import time
print("This is spin the wheel")
print()
print("How many numbers do you want there to be on the wheel")
number = int(input())
wheel = random.randint(0,number)
print("The Number is...")
print()
time.sleep(2.5)
print(wheel)
