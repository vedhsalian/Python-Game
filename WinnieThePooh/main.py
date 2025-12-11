import pgzrun
from random import randint

WIDTH=800
HEIGHT=500

STARTTIME=10
time=10
score=0
gameover=False

winnie=Actor('winnie')
winnie.pos=50,50

hunny=Actor('hunnypot')
hunny.pos=400,250

def draw():
    screen.blit('winniebg', (0,0))

    winnie.draw()
    hunny.draw()

    screen.draw.text("Score= "+str(score),midtop=(400,0),fontsize=30,color="black")

    if gameover:
        screen.fill("black")
        screen.draw.text("Game Over",fontsize=80,color="red",center=(400,150))
        screen.draw.text("Your Final Score was "+str(score),fontsize=40,color="blue",center=(400,350))


def update():
    global time
    global score
    if keyboard.a:
        winnie.x-=2
    
    if keyboard.d:
        winnie.x+=2
    
    if keyboard.w:
        winnie.y-=2
    
    if keyboard.s:
        winnie.y+=2

    if keyboard.left:
        hunny.x-=2
    
    if keyboard.right:
        hunny.x+=2
    
    if keyboard.up:
        hunny.y-=2
    
    if keyboard.down:
        hunny.y+=2

    hunnycaught=winnie.colliderect(hunny)

    if hunnycaught:
        score+=10
        time=STARTTIME
        place_hunny()

def place_hunny():
    hunny.x=randint(50,WIDTH-50)
    hunny.y=randint(50,HEIGHT-50)

def time_up():
    global gameover
    gameover=True
clock.schedule(time_up,time)

pgzrun.go()