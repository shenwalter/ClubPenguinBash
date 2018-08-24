import pyautogui, time
time.sleep(3)
distance = 800

while True:
    pyautogui.moveRel(distance, 0, duration=0.5)
    pyautogui.click()
    time.sleep(4)
    pyautogui.typewrite("D")
    time.sleep(14)
    pyautogui.moveRel(-distance, 0, duration=0.5)
    pyautogui.click()
    time.sleep(4)
    pyautogui.typewrite("D")
    time.sleep(14)
