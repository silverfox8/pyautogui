import pyautogui
from time import sleep
import random
#print(pyautogui.position())

for i in range(100):
	i=i+1
	screen_shot = pyautogui.screenshot(region=(630,139,2580,1837))#487,139,2865,1837
	sleep(random.uniform(0.8,2.5))
	screen_shot.save('Dekiru_' + str(i) + '.png')
	pyautogui.moveTo(1819,2037)
	pyautogui.click()
	pyautogui.moveTo(968,2047) #taihi
	sleep(1)

	