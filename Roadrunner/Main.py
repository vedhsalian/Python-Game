import pgzrun
from random import randint

WIDTH=800
HEIGHT=500

score=0
game_over=False
time=10

wile=Actor('wileecoyote')
wile.pos=100,100

runner=Actor('roadrunner')
runner.pos=400,250

def draw():
    screen.blit('roadrunnerbg',(0,0))

    wile.draw()
    runner.draw()

    screen.draw.text("Score: "+str(score),midtop=(400,0,), fontsize=40, color="orange")

    if game_over:
        screen.fill("black")
        screen.draw.text("GAME OVER",center=(400,150), fontsize=80, color="red")
        screen.draw.text("Your Final Score is: "+str(score), center=(400,350), fontsize=40, color="blue")

def update():
    global score
    global time

    if keyboard.left:
        runner.x-=2

    if keyboard.right:
        runner.x+=2
    
    if keyboard.up:
        runner.y-=2

    if keyboard.down:
        runner.y+=2
    
    if keyboard.a:
        wile.x-=2
    
    if keyboard.d:
        wile.x+=2

    if keyboard.w:
        wile.y-=2
    
    if keyboard.s:
        wile.y+=2
    
    runnercaught=wile.colliderect(runner)

    if runnercaught:
        score+=10
        timecap=10-time
        time+=timecap
        place_runner()

def place_runner():
    runner.x=randint(50,WIDTH-50)
    runner.y=randint(50,HEIGHT-50)

def times_up():
    global game_over
    game_over=True

clock.schedule(times_up,time)

pgzrun.go()