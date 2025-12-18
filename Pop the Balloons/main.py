import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=500

score=0
balloons=[]
spawn_interval=2.00
start_time=0
total_time=0
end_time=60.00
last_spawn_time=time()

dart=Actor('dart')
dart.pos=400,450

def draw_balloons():
    global total_time,last_spawn_time,end_time
    total_time=time()-start_time
    if total_time<end_time:
        if time()-last_spawn_time>spawn_interval:
            rballoon=Actor('rballoon')
            rballoon.pos=randint(50,750),50
            balloons.append(rballoon)
            last_spawn_time=time()

def draw():
    screen.fill("black")

    dart.draw()

def update():
    if keyboard.a:
        dart.x-=2

    if keyboard.d:
        dart.x+=2

    if keyboard.space:
        if dart.y>0:
            dart.y-=50
        else:
            dart.y=450
    
    if keyboard.r:
        dart.y=450
    
    #balloon_popped=dart.colliderect(rballoon)
    #if balloon_popped:
        #score+=10

draw_balloons()

pgzrun.go()