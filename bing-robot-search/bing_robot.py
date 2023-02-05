import time
import pyautogui
import os
import random
import string

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

search_amount = int(input("Enter the amount of searchs you want to perform: "))

os.system("google-chrome --new-tab")
pyautogui.click(x=0, y=50)
pyautogui.click(pyautogui.locateCenterOnScreen(
    "images/search-bar.png", confidence=0.5), duration=1)
time.sleep(1)

pyautogui.typewrite("https://www.bing.com/ \n")

for i in range(search_amount):
    term = ''.join(random.choice(string.ascii_letters)
                   for i in range(5)) + " \n"
    pyautogui.typewrite(term, interval=0.10)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        "images/bing-search-bar.png", confidence=0.5))
    time.sleep(2)
pyautogui.alert(text="Done!", title="Aviso do sistema", button="OK")
