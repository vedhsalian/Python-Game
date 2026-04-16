import pygame
import time
import gif_pygame
import sys

pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Recycling")

redbin=pygame.image.load("Recycling/Images/Bin.png")
redbin=pygame.transform.scale(redbin,(250,250))
redbinsprite=redbin.get_rect()
redbinsprite.center=(100,600)

greenbin=pygame.image.load("Recycling/Images/Recyclebin.png")
greenbin=pygame.transform.scale(greenbin,(250,250))
greenbinsprite=greenbin.get_rect()
greenbinsprite.center=(650,600)

can=pygame.image.load("Recycling/Images/Can.png")
can=pygame.transform.scale(can,(80,80))
cansprite=can.get_rect()
cansprite.center=(100,250)

chips=pygame.image.load("Recycling/Images/Chips (2).png")
chips=pygame.transform.scale(chips,(80,80))
chipssprite=chips.get_rect()
chipssprite.center=(250,250)

plastic=pygame.image.load("Recycling/Images/Plastic.png")
plastic=pygame.transform.scale(plastic,(80,80))
plasticsprite=plastic.get_rect()
plasticsprite.center=(400,250)

bottle=pygame.image.load("Recycling/Images/WaterBottle.png")
bottle=pygame.transform.scale(bottle,(80,80))
bottlesprite=bottle.get_rect()
bottlesprite.center=(550,250)

text_font1=pygame.font.SysFont("Impact", 50)
f1=text_font1.render("Welcome to the Recycling Activity", True, (0,255,0))
f1rect=f1.get_rect()
f1rect.center=(400,30)

text_font2=pygame.font.SysFont("Arial", 25)
f2=text_font2.render("Drag the recyclable trash to the green bin and the non-recyclable trash to the red bin", True, (255,165,0))
f2rect=f2.get_rect()
f2rect.center=(400,100)

dragging=False
dragging2=False
dragging3=False
dragging4=False
gameloop=True

while gameloop:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if cansprite.collidepoint(event.pos):
                dragging=True
            if chipssprite.collidepoint(event.pos):
                dragging2=True
            if plasticsprite.collidepoint(event.pos):
                dragging3=True
            if bottlesprite.collidepoint(event.pos):
                dragging4=True

        if event.type==pygame.MOUSEMOTION and dragging==True:
            cansprite.x= event.pos[0]
            cansprite.y=event.pos[1]
        if event.type==pygame.MOUSEMOTION and dragging2==True:
            chipssprite.x= event.pos[0]
            chipssprite.y=event.pos[1]
        if event.type==pygame.MOUSEMOTION and dragging3==True:
            plasticsprite.x= event.pos[0]
            plasticsprite.y=event.pos[1]
        if event.type==pygame.MOUSEMOTION and dragging4==True:
            bottlesprite.x= event.pos[0]
            bottlesprite.y=event.pos[1]
        
        if event.type==pygame.MOUSEBUTTONUP:
            dragging=False
            dragging2=False
            dragging3=False
            dragging4=False

        if cansprite.colliderect(greenbinsprite) and dragging==False:
            cansprite.center=(10000,10000)
        if bottlesprite.colliderect(greenbinsprite) and dragging==False:
           bottlesprite.center=(10000,10000)
        if plasticsprite.colliderect(redbinsprite) and dragging==False:
            plasticsprite.center=(10000,10000)
        if chipssprite.colliderect(redbinsprite) and dragging==False:
            chipssprite.center=(10000,10000)
        

    screen.fill("black")
    screen.blit(redbin,redbinsprite)
    screen.blit(greenbin,greenbinsprite)
    screen.blit(can,cansprite)
    screen.blit(chips,chipssprite)
    screen.blit(plastic,plasticsprite)
    screen.blit(bottle,bottlesprite)
    screen.blit(f1,f1rect)
    screen.blit(f2,f2rect)
    pygame.display.flip()

pygame.quit()