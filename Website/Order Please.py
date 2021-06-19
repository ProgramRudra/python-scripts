print('Welcome To The India Hut')
print('Here is the Menu')
print('\nNaan: $2.99\n'
      'Biryani:$10.00\n'
      'Paneer: $5.99\n'
      'Dal: $3.99')

a = 0

print('\nHow much items do you want?')
num = int(input())
for i in range(num):
    print('Enter Item')
    item = str(input())
    if item == 'Naan':
        a += 2.99
    elif item == 'Biryani':
        a += 10.00
    elif item == 'Paneer':
        a += 5.99
    elif item == 'Dal':
        a += 3.99
    else:
        exit()
print('Your total is ', a)
