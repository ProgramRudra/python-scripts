print ('how many lines')
line = int(input())
first_half = int(line / 2)
a=0
c = first_half + 1 
second_half = int(line / 2)
b = second_half

for i in range (1, line+1):
  
    if (i <=c):
        space=int(c-i)
        star=int(line - 2*(c-i))
        print (space*' ',star*'*')
    else:
        space=int(i-c)
        star=int(line - 2*(i-c))
        print (space*' ',star*'*')
