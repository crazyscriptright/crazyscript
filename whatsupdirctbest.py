
#Happy Birthday in Python
from ctypes import sizeof 
import pyautogui as pg
import time
from random import randint
time.sleep(10)
space =''
a=60
name="SUNNY"
for i in range (1,100):
    count = randint (1, 50)
    tem=count
    while(count > 0):
        space +=' '
        count -= 1
    if(i%10==0):
        pg.press(".")
        pg.typewrite('* HAPPY Birthday!'+ space )
        for j in range(a-tem-20):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%9 == 0):
        pg.press(".")
        pg.typewrite(space + '*')
        for j in range(a-tem):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")         
    elif(i%8==0):
        pg.press(".")
        pg.typewrite(space+name)
        for j in range(a-tem-22):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%7==0):
        pg.press(".")
        pg.typewrite(space+"*")
        for j in range(a-tem):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%6==0):
        pg.press(".")
        pg.typewrite(space+"HappyBirthday!")
        for j in range(a-tem-22):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%5==0):
        pg.press(".")
        p=pg.typewrite(space+"*")  
        print(tem)
        for j in range(a-(tem)):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i==3):
        pg.press(".")
        pg.typewrite(space+"Wish You")
        for j in range(a-tem-22):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%3==0 & i!=3):
        pg.press(".")
        pg.typewrite(space+name)
        for j in range(a-tem-22):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    elif(i%9==1):
        pg.press(".")
        pg.typewrite(space+"Keep Smiling")
        for j in range(a-tem-20):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")
    else:
        pg.press(".")
        for j in range(a+2):
            pg.typewrite(" ")
        pg.press(".")
        pg.press("enter")        
    space=''
    time.sleep(0.2)   