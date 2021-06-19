import random
while True:
    print('Rock Paper Scissors')
    ans = str(input())
    if ans=='Rock':
        c = random.randint(1, 3)
        if c==1:
            print('I Choose Rock')
            print ('Which Means It is A Tie')
            print()
        elif c==2:
            print('I Choose Scissors')
            print ('That Means You Win')
            print()
        elif c==3:
            print ('I Choose Paper')
            print ('That Means I Win')
            print()
        else:
            print ('Try Again')
    elif ans=='Scissors':
        d = random.randint(1, 3)
        if d==1:
            print('I Choose Rock')
            print('That Means I Win')
            print()
        elif d==2:
            print('I Choose Scissors')
            print('That Means It is A Tie')
            print()
        elif d==3:
            print('I Choose Paper')
            print ('That Means You Win')
            print()
        else:
            print('Try Again')
    elif ans=='Paper':
        e = random.randint(1, 3)
        if e==1:
            print('I Choose Rock')
            print('That Means You Win')
            print()
        elif e==2:
            print('I Choose Scissors')
            print('That Means I Win')
            print()
        elif e==3:
            print('I Choose Paper')
            print('That Means It i  s A Tie')
            print()
        else:
            print ('Try Again')
    else:
        print('Try Again')
