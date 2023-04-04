import pyautogui
import time
import keyboard

while True:
    # move the mouse to a new location
    pyautogui.moveTo(100, 100, duration=0.25)
    
    # wait for a few seconds
    time.sleep(5)
    
    # move the mouse to another location
    pyautogui.moveTo(200, 200, duration=0.25)
    
    # wait for a few seconds
    time.sleep(5)
    
    # check if the 'q' key is pressed
    if keyboard.is_pressed('q'):
        break
