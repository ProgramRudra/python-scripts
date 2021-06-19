import random
print ("what is the first value you want for guessing the number")
b = int(input())
print ("What is the second value you want for guessing the number")
f = 'read'
c = int(input())
a = int((random.randint(b, c)))
while f=='read':
    print("Guess the number it is up to",c)
    d = int(input())
    if d > a:
        print("Your number is to high")
    elif d < a:
        print("Your number is to low")
    else:
        print("Correct")
        quit()
print("The number was", a)
quit()
