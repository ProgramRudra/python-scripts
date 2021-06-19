import time
import os
import wave
print ("This is Python Timer ")
#print()
print()
print ("Please select - Hours OR Minutes OR Seconds")
choose = str(input())
#print (choose)
if choose=='seconds':
    print('enter seconds')
    seconds = int(input())
  #  print ("Print Value")
    time.sleep(seconds)

    print ('wake up')

elif choose == 'minutes':
    print('enter minutes')
    minutes = int(input())
   # print("Print Value")
    time.sleep(minutes * 60)
    print ('wake up')

elif choose=='hours':
    hours = int(input())
  #  print ('Print Value')
    time.sleep(hours * 3600)
    print('wake up')

else:
    print ('Restart Program')
    exit()
