import pyautogui as pg
import webbrowser as wb
import time

# wb.open("web.whatsapp.com")
time.sleep(10)
for i in range(20):
    pg.typewrite("Happy birthday to you sunny")
    pg.press("Enter")
