import time 
import os 
import pygame

pygame.init()

stopwatch = 0

noise = pygame.mixer.Sound('extremely-loud-correct-buzzer.mp3')

main = input("\ntimer or stopwatch? T/S?\n")

#stopwatch stuff
if main == "S":
	while True:
		stopwatch = stopwatch + 0.1
		time.sleep(0.1)
		print(stopwatch)


#timer stuff
if main == "T":
	timeramount = int(input("how much time do you want your timer to last for?\n"))
while True:
	timeramount = timeramount - 0.1
	time.sleep(0.1)
	print(timeramount)
	if timeramount <= 0:
		print("YOUR TIMER IS DONE!")
		noise.play()
		time.sleep(2)
		break
