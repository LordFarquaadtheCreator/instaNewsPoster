import pyautogui
import time

times = 5  # time to wait
for i in range(times):
    print(i+1)
    time.sleep(1)

print(pyautogui.position())
