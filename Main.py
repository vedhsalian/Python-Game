import pgzrun
from random import randint

WIDTH=600
HEIGHT=600

tom=Actor('tom')
tom.pos=100,100

jerry=Actor('jerry')
jerry.pos=200,200

score=0
game_over=False

def draw():
    screen.blit('tomandjerrybg',(0,0))

    tom.draw()
    jerry.draw()

    screen.draw.text('Score='+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Time's Up",midtop=(300,10),fontsize=40,color="red")

def place_jerry():
    jerry.x=randint(50,WIDTH-50)
    jerry.y=randint(50,HEIGHT-50)

def update():
    global score
    if keyboard.left:
        tom.x-=2
    
    if keyboard.right:
        tom.x+=2
    
    if keyboard.up:
        tom.y-=2

    if keyboard.down:
        tom.y+=2

    jerrycaught=tom.colliderect(jerry)

    if jerrycaught:
        score+=10
        place_jerry()

def time_up():
    global game_over
    game_over=True

clock.schedule(time_up,60.0)

pgzrun.go()