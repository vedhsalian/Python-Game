import pygame
import time
import gif_pygame
import sys

pygame.mixer.init()
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Mario Game")

FPS=60
clock=pygame.time.Clock()

retrosong="Mario Game/Music/Tank Tank.mp3"
pygame.mixer.music.load(retrosong)
pygame.mixer.music.play(-1)

deathsound="Mario Game/Music/Deathsound.mp3"

BG=pygame.image.load("Mario Game/Images/SkyBG.webp").convert_alpha()
BG=pygame.transform.scale(BG,(800,800))

Grass=pygame.image.load("Mario Game/Images/Grass.webp").convert_alpha()
Grass=pygame.transform.scale(Grass,(1600,80))
GrassSprite=Grass.get_rect()
GrassSprite.center=(400,760)

gif_image=gif_pygame.load("Mario Game/GIFs/MarioRun.gif")
goomba_gif=gif_pygame.load("Mario Game\GIFs/goomba.gif")

score=0
text_font1=pygame.font.SysFont("Arial", 30)
f1=text_font1.render("SCORE: {}".format(score), True, (0,0,255))
f1rect=f1.get_rect()
f1rect.center=(100,30)

vy = 0
gravity = 0.8
jump_strength = -20
is_jumping = False
is_dead=False
mx=100
my=720
ex=700
ey=690
vx=5
ev=2
gh=65
gameloop=True

current_frame_surface = gif_image.blit_ready()
scaled_frame = pygame.transform.scale(current_frame_surface,(80,80))
frame_rect=scaled_frame.get_rect(center=(mx,my))

while gameloop:
    pygame.time.delay(10)

    GrassSprite.x-=vx

    current_frame_surface2 = goomba_gif.blit_ready()
    scaled_frame2 = pygame.transform.scale(current_frame_surface2,(65,gh))
    ex-=ev
    frame_rect2=scaled_frame2.get_rect(center=(ex,ey))

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            gameloop=False

        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_a] and frame_rect.x>20 and not is_dead:
            frame_rect.x-=20
        if keys[pygame.K_d] and frame_rect.x<720 and not is_dead:
            frame_rect.x+=20
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE] and not is_jumping:
                vy = jump_strength
                is_jumping = True
    
    if abs(frame_rect.x-frame_rect2.x)<30 and not is_jumping and not is_dead:
        is_dead=True
        pygame.mixer.music.stop()
        pygame.mixer.music.load(deathsound)
        pygame.mixer.music.play(1)
        text_font1=pygame.font.SysFont("Arial", 100)
        f1=text_font1.render("GAME OVER", True, (255,0,0))
        f1rect.center=(200,400)
        ev=0
        vx=0
    
    if is_jumping and abs(frame_rect.x-frame_rect2.x)<15 and frame_rect.y-frame_rect2.y<-15 and not is_dead:
        while gh>0:
            gh-=0.1

        ex=1600
        gh=65
        
    vy+=gravity
    frame_rect.y+=vy

    if frame_rect.bottom >= 720:
        frame_rect.bottom = 720
        vel_y = 0
        is_jumping = False

    if GrassSprite.x<=-400:
        GrassSprite.x=0
    if ex<=0:
        ex=800
    screen.blit(BG,(0,0))
    screen.blit(Grass,GrassSprite)
    screen.blit(scaled_frame,frame_rect)
    screen.blit(scaled_frame2,frame_rect2)
    screen.blit(f1,f1rect)

    pygame.display.flip()

pygame.quit()

#HW: Add a scoreboard.