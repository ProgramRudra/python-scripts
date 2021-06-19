print ('how many lines')
line = int(input())
first_half = int(line / 2)
a=0
c = first_half + 1 
second_half = int(line / 2)
b = second_half
#Below code is example of "for loop"
#for i in range(1, c):
#    a += 1
#    print (a*'*')
#for i in range (1, second_half):
#    b -= 1
#    print (b*'*')
#Below code is exampel of "for loop" and "IF/Else "
for i in range (1,line+1):
    if (i <= c):
        a += 1
        print (a*'*')
    else:
        b-= 1
        print (b*'*')

    

    

