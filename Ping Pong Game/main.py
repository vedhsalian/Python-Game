import pygame

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Ping Pong Game")

hitsfx="Ping Pong Game/HitSFX.mp3"
pygame.mixer.music.load(hitsfx)

racket1=pygame.image.load("Ping Pong Game/Images/Racket1.png").convert_alpha()
racket1=pygame.transform.scale(racket1,(80,80))
racket1Sprite=racket1.get_rect()

racket2=pygame.image.load("Ping Pong Game/Images/Racket2.png").convert_alpha()
racket2=pygame.transform.scale(racket2,(90,90))
racket2Sprite=racket2.get_rect()

Ball=pygame.image.load("Ping Pong Game/Images/Ball.png").convert_alpha()
Ball=pygame.transform.scale(Ball,(30,30))
BallSprite=Ball.get_rect()

racket1Sprite.center=(25,400)
racket2Sprite.center=(775,400)
bx=400
by=400
BallSprite.center=(bx,by)

gameloop=True

HEIGHT=800
WIDTH=800

score1=0
score2=0

font1=pygame.font.SysFont("Impact",20)

text1=font1.render("RACKET 1 SCORE: "+str(score1),True,"blue")
text2=font1.render("RACKET 2 SCORE: "+str(score2),True,"red")

dx=0.2
dy=0.2
is_touching=False

while gameloop:
    bx+=dx 
    by+=dy

    if by>800:
        dy*=-1
    if by<0:
        dy*=-1

    if bx<0:
        score2+=1
        bx=400
        by=400
        text2=font1.render("RACKET 2 SCORE: "+str(score2),True,"red")
        dx*=-1
    if bx>800:
        score1+=1
        bx=400
        by=400
        text1=font1.render("RACKET 1 SCORE: "+str(score1),True,"blue")
        dx*=-1

    if BallSprite.colliderect(racket1Sprite) and is_touching==False:
        dx=-0.2
        dy=-0.2
        bx+=50
        by+=50
        print(dx,dy)
        pygame.mixer.music.play(1)
        is_touching=True
    if BallSprite.colliderect(racket2Sprite) and is_touching==False:
        dx=0.2
        dy=0.2
        print(dx,dy)
        pygame.mixer.music.play(1)
        is_touching=True
    if BallSprite.clipline((400,0),(400,800)):
        is_touching=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
            
        keys=pygame.key.get_pressed()

        if keys[pygame.K_a] and racket1Sprite.x>40:
            racket1Sprite.x-=50
        if keys[pygame.K_d] and racket1Sprite.x<400-120:
            racket1Sprite.x+=50
        if keys[pygame.K_w] and racket1Sprite.y>40:
            racket1Sprite.y-=50
        if keys[pygame.K_s] and racket1Sprite.y<680:
            racket1Sprite.y+=50

        if keys[pygame.K_j] and racket2Sprite.x>440:
            racket2Sprite.x-=50
        if keys[pygame.K_k] and racket2Sprite.y<680:
            racket2Sprite.y+=50
        if keys[pygame.K_i] and racket2Sprite.y>40:
            racket2Sprite.y-=50
        if keys[pygame.K_l] and racket2Sprite.x<720:
            racket2Sprite.x+=50

    if by>800:
        dy*=-1
    if by<0:
        dy*=-1
    
    if bx<0:
        score2+=1
        bx=400
        by=400
        text2=font1.render("RACKET 2 SCORE: "+str(score2),True,"red")
        dx*=-1
    if bx>800:
        score1+=1
        bx=400
        by=400
        text1=font1.render("RACKET 1 SCORE: "+str(score1),True,"blue")
        dx*=-1
    
    if BallSprite.colliderect(racket1Sprite):
        dx*=-1
        dy*=-1
    if BallSprite.colliderect(racket2Sprite):
        dx*=-1
        dy*=-1

    if score1-score2>=5:
        print("Player 1 Wins!")
        gameloop=False

    if score2-score1>=5:
        print("Player 2 Wins!")
        gameloop=False

    screen.fill((0,0,0))
    screen.blit(racket1,racket1Sprite)
    screen.blit(racket2,racket2Sprite)
    screen.blit(Ball,BallSprite)
    screen.blit(text1,(10,10))
    screen.blit(text2,(650,10))
    BallSprite.center=(bx,by)
    pygame.draw.line(screen,"white",(400,0),(400,800),width=2)
    pygame.display.update()

pygame.quit()