import time, pyautogui, datetime

timeout = time.time() + 3000

while time.time() < timeout:
    pyautogui.move(100,100)
    time.sleep(60)
    pyautogui.move(-100, -100)
    time.sleep(60)
else:
    pyautogui.alert('Time limit reached', 'mouseMover')
'OK'


