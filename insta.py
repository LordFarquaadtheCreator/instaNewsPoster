import webbrowser
import pyautogui
import time
import photopeaSaver
import summerizer

pyautogui.FAILSAFE = True

timeDelay = 2
"""
ONLY  USE  WHEN  YOU  HAVE  PHOTOPEA  OPEN  AND  IMAGE  DONE
.

"""
photopeaSaver.savePhoto(timeDelay, blur=True)  # self expanitory, really

webbrowser.open("https://www.instagram.com/rightondigitalofficial/")

time.sleep(2.5 + timeDelay)
pyautogui.click(72, 570)  # create
time.sleep(2)
pyautogui.click(730, 592)
# now the select photo thingie is open

time.sleep(0.8)
pyautogui.click(1011, 240)  # clicks search bar
pyautogui.typewrite("Instagram Post", interval=0)
time.sleep(1.2)
pyautogui.click(587, 349)  # clicks image
pyautogui.click(1062, 662)  # clicks enter
# opens the post successfully

time.sleep(0.5)
pyautogui.click(969, 223)  # clicks past cropping
time.sleep(0.3)
pyautogui.click(1142, 218)  # clicks past filters
time.sleep(0.3)

pyautogui.click(895, 340)  # clicks on text box
# text = input()
# time.sleep(2)
# pyautogui.typewrite(summerizer.summerize(text))
pyautogui.typewrite(
    "\nYeah, we did that! Check out this, and more with the link in bio!\n.\n.\n.\n"
)

pyautogui.click(550, 519)  # clicks at image to start tagging
