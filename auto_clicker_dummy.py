import pyautogui
import keyboard
import time

time.sleep(3)

pyautogui.moveTo(1150, 325)

try: 
    while True:
        x, y = pyautogui.position()
        if keyboard.is_pressed('q'):
            print('Stopping the script')
            break

        pyautogui.click()

except KeyboardInterrupt:
    print('Script stopped by the user')