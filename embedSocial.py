import webbrowser
import pyautogui
import time

timeDelay = 0
webbrowser.open(
    'https://embedsocial.com/admin/feedlink/editor/14f64cc45c1b51d6c0141acc54dd38faf29bee2a')

time.sleep(2+timeDelay)
pyautogui.click(500,500) #focus to website
pyautogui.click(88, 65)  # refresh
time.sleep(6)

pyautogui.click(721, 809)  # click on post
time.sleep(.2)
pyautogui.click(493, 432)
time.sleep(.2)
pyautogui.click(473, 585)
time.sleep(.2)
pyautogui.click(447, 522)  # select new label

pyautogui.typewrite('Read')
pyautogui.click(307, 611)
pyautogui.rightClick()
pyautogui.click(369, 719)  # paste link (copied before)
time.sleep(.5)
pyautogui.click(351, 678)  # click done
