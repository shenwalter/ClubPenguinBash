import pyautogui, time, sys
time.sleep(3)
distance = 500

while True:
    for x in range(450, 1000, 50):
        for y in range(600,750,50):
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(2)
            pyautogui.typewrite("D")
            time.sleep(14)
    pyautogui.moveTo(400, 550)
    pyautogui.click()
    time.sleep(7)
#y: [600:700]
#x: [450:950]
##while True:
##    x, y = pyautogui.position()
##    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
##    print(positionStr, end='')
##    print('\b' * len(positionStr), end='', flush=True)
