import webbrowser
import pyautogui
import time
pyautogui.FAILSAFE = True

delay = 1
webbrowser.open('https://rightondigital.com/')  # righton is open

webbrowser.open('https://www.photopea.com/')  # photopea is open
time.sleep(3+delay)
pyautogui.click(650,200)
pyautogui.click(650, 340)  # open finder

time.sleep(.8)
pyautogui.click(1015, 241)  # clicks search bar
pyautogui.typewrite('instaPost.psd', interval=0)
time.sleep(1)

pyautogui.click(577, 364)  # clicks on psd

pyautogui.click(1082, 652)  # opens!!!!
