import pyautogui

#moves the mouse to the start menu and shutdowns the pc. Maybe one day make it a script.
def MovetoStart():
        pyautogui.click(26, 1057)
        pyautogui.click(40, 1024)
        pyautogui.click(17, 943)
        pyautogui.click(17, 943)


MovetoStart()