import pygame
import time
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Birthday Card")

FPS=60
clock=pygame.time.Clock()

image1=pygame.image.load("Birthday Card Animation/BDayBG1.jpg")
image1=pygame.transform.scale(image1,(800,600))


image2=pygame.image.load("Birthday Card Animation/BDayBG2.webp")
image2=pygame.transform.scale(image2,(800,600))

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False

    screen.blit(image1,(0,0))
    pygame.display.update()
    time.sleep(4)
    screen.blit(image2,(0,0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()