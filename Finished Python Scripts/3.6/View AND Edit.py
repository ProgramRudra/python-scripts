print ('Do you want to view a file or edit')
ans = input()
if ans=='edit':
    print ('Type the Filename you want to edit')
    filename = input()
    write = open(filename, 'a')
    #num = int(input ('How many times do you want to write lines: '))
    while True:
        print ('What is the string you want to type')
        string = str(input())
        print ('Type in EXIT to quit program')
        if string !='EXIT':
            write.write(string)
            write.write('\n')
        else:
            quit('Exiting...')

elif ans=='view':
    a = input('Write target of file please include the extension')
    b = open(a, 'r')
    read_1 = (b.read())
    print(read_1)
else:
    print('Error\nChoose view or edit')