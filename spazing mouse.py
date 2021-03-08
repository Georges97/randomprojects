import pyautogui

def Move100():
    for i in range(100): # Move mouse in a square.
        pyautogui.moveTo(100, 100, duration=0.05)
        

def MovetoStart():
        pyautogui.click(26, 1057)
        pyautogui.click(40, 1024)
        pyautogui.click(17, 943)
        pyautogui.click(17, 943)



pyautogui.position()

#pyautogui.mouseInfo()


#print(p)
#Move100()
MovetoStart()