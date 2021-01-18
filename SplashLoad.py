import pygame
import time

import Verification as OTP
import Lock_Screen as log
import Slambook as book

pygame.init()
screen=pygame.display.set_mode((500,300))

background=pygame.image.load('SplashScreen.png')
loadData=pygame.image.load('load.png')

chance = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.blit(background,(0,0))

    if(log.ok()==True and chance==1):
        for i in range(20,200,20):
            screen.blit(loadData,(i,235))
        chance = 2
    
    elif(OTP.ok()==True and chance==2):
        for i in range(20,280,20):
            screen.blit(loadData,(i,235))
        chance = 3

    elif(book.ok()==True and chance==3):
        for i in range(20,480,20):
            screen.blit(loadData,(i,235))
        chance = 4
    
    pygame.display.update()
    time.sleep(1)

    if(chance==4):
        time.sleep(2)
        break
 