import os
print('Type in Command ')
while True:
    command = input()
    run = os.system(command)
    print(run)