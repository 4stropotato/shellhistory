import keyboard
import time


kb_list = [] #data storage for the previous command

def goto():
	x = -1
	arr = kb_list[x]
	keyboard.write(arr)
	while True:
	    if keyboard.is_pressed('up'):
	        x = x - 1
	        print(x)
	        time.sleep(0.1)
	        keyboard.release('up')
	    elif keyboard.is_pressed('down'):
	        x = x + 1
	        print(x)
	        time.sleep(0.1)
	        keyboard.release('down')
	    elif keyboard.is_pressed('enter'):
	    	break

def shell():
	while True:
		x = input()
		if keyboard.is_pressed('up'):
			goto()
		kb_list.append(x)

shell()
