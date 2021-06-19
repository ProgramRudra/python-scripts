# %s replaces a string or integer in to its place

print ("How much dollars do you have")
money = int(input())
mymoney = 200
print ('I have %s dollars'%mymoney)
a = int(mymoney-money)
b = int(money-mymoney)
if money==mymoney:
    print ('We have the same amount of money')
elif money>mymoney:
    print ("You have %s dollars more then me" %b)
elif money<mymoney:
    print ("I have %s more dollars then you" %a)