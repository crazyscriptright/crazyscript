'''Happy Birthday in Python Code
- The Original One'''
import time
from random import randint

for i in range(1, 35):
    print('')

space = ''
for i in range(1, 1000):  # 1000 is number of message you want to send
    count = randint(1, 35)
    while(count > 0):
        space += ' '
        count -= 1
    if(i % 10 == 0):
        print(space + 'Keep Smiling')
    elif(i % 9 == 0):
        print(space + "ð")
    elif(i % 5 == 0):
        print(space + "ðHappy Birthday!")
    elif(i % 8 == 0):
        print(space + "ð")
    elif(i % 7 == 0):
        print(space + "ð«")
    elif(i % 6 == 0):
        print(space + "ANANDAð")
    elif(i % 4 == 0):
        print(space + "ð")
    else:
        print(space + "ð¸")
    space = ''
    time.sleep(0.2)
