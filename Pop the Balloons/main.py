import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=500

score=0
balloons=[]
spawn_interval=2.00
start_time=time()
total_time=0
end_time=1.00
last_spawn_time=time()
game_over=False
dart_shooting=False

DART_SPEED=5
BALLOON_SPEED=1

dart=Actor('dart')
dart.pos=400,450

def draw():
    screen.fill("black")

    dart.draw()

    for balloon in balloons:
        balloon.draw()
    
    if game_over:
        screen.draw.text("GAME OVER", center=(400,200), color="red", fontsize=80)
        screen.draw.text("Your Final Score is: "+str(score), color="blue", center=(400,300), fontsize=60)
    
    screen.draw.text("Score: "+str(score), topleft=(20,20), color="white",)

def update():
    global last_spawn_time, score, dart_shooting, game_over

    if time() - start_time>=end_time:
        game_over=True
        return

    if keyboard.a:
        dart.x-=2

    if keyboard.d:
        dart.x+=2

    if keyboard.space:
        dart_shooting=True
    
    if dart_shooting:
        dart.y-=DART_SPEED
    
    if dart.y <= 0:
        dart.y=450
        dart_shooting=False

    if time()-last_spawn_time>spawn_interval:
        rballoon=Actor('rballoon')
        rballoon.pos=randint(50,750),50
        balloons.append(rballoon)
        last_spawn_time=time()

    for rballoon in balloons:
        rballoon.y+=BALLOON_SPEED
        if rballoon.y>=HEIGHT:
            balloons.remove(rballoon)

    for rballoon in balloons:
        if dart.colliderect(rballoon):
            balloons.remove(rballoon)
            score+=10
            dart.y=450
            dart_shooting=False


pgzrun.go()