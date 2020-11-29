sec = 3
print('spam code will start in '+str(sec)+' seconds')
import pynput
from pynput.keyboard import Key, Controller
import time
Keyboard = Controller()
time.sleep(sec)
a = 1
while true:
    b = str(a)
    if a == 6: # loop limit
        break
    for x in "hey, this is spam":
        Keyboard.press(x)
        Keyboard.release(x)
    a+=1 # or a++ -idk-
    time.sleep(0.5) # message time per second || 0.5 = 500ms  
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
