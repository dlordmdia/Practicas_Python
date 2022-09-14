import pyautogui as pt
import time

limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)
pt.press("enter")

while i < int(limit):
    pt.typewrite(message)    
    
    pt.press("enter")

    i+=1