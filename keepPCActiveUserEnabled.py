import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None
count = 0
prev_x, prev_y = pyautogui.position()

if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    numMin = 1
else:
    numMin = int(sys.argv[1])

while True:
    x = 0
    user_active = False
    
    # Check if the user is active every minute
    while x < numMin:
        time.sleep(60)
        x += 1
        curr_x, curr_y = pyautogui.position()
        if curr_x != prev_x or curr_y != prev_y:
            user_active = True
            prev_x, prev_y = curr_x, curr_y
            break
    
    if user_active:
        print("User is active, skipping this cycle")
        continue

    # Perform mouse movement if user is not active
    for i in range(0, 200):
        pyautogui.moveTo(0, i * 4)
        x1, y1 = pyautogui.position()
        if x1 > 0:
            break

    pyautogui.moveTo(1, 1)
    for i in range(0, 3):
        pyautogui.press("shift")

    print("Movement made at {}".format(datetime.now().time()))
    count += 1
    print("Count: ", count)
    # Update the previous position
    prev_x, prev_y = pyautogui.position()
