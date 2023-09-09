import pyautogui
import time
pyautogui.FAILSAFE = True


def savePhoto(timeDelay=0, blur=False):
    time.sleep(.8)

    if blur == True:
        # blurs background
        pyautogui.click(255, 133)  # filter
        pyautogui.click(410, 388)  # blur
        pyautogui.click(502, 520)  # guasian blur
        time.sleep(0.5)
        pyautogui.click(531, 315)  # save

    pyautogui.click(22, 128)  # file
    pyautogui.click(120, 419)  # export as
    pyautogui.click(231, 419)  # png

    pyautogui.click(760, 474)
    # click save (doesn't download yet)
    pyautogui.click(799, 244)
    time.sleep(.5)
    pyautogui.typewrite('Instagram Post')
    # renames file to replace old one

    pyautogui.press('enter')
    time.sleep(.2)
    pyautogui.click(770, 545)

    time.sleep(1)
    pyautogui.click(1421, 876)  # closes download bar
    pyautogui.click(632, 283)  # closes "disable adblocker popup"
