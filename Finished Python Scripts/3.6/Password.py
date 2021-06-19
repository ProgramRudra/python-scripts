password = 'allpass'
while password=='allpass':
    print("enter password to see the programs script")
    a = input()
    if a!=password:
        print("Try Again")
        a = input()

    else:
        print("Correct")
        b = open("c:/Users/Rudra/Documents/Working On Python Scripts/3.6/Password.py", "r")
        read_1 = (b.read())
        print(read_1)
        quit()