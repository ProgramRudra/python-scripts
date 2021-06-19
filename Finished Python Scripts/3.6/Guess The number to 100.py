import random
a = int((random.randint(1, 101)))
for i in range(5):
    print("Guess the number it is up to 100")
    b = int(input())
    if b > a:
        print("Your number is to high")
    elif b < a:
        print("Your number is to low")
    else:
        print("Correct")
        quit()
print("The number was", a)
quit()