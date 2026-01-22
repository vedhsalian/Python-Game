import pgzrun
from random import randint

TITLE="UFO Defense"

OBJECTIVE="Objective : Shoot down all the UFOs soldier!"

ufos=10
lives=3
game_over=False
game_complete=False
message=""

WIDTH=800
HEIGHT=800

ufo=Actor('ufo')

def draw():
    screen.fill("black")
    if not game_complete and not game_over:
        ufo.draw()
    screen.draw.text("Lives : "+str(lives), topright=(780,20), color="red")
    screen.draw.text("UFOs : "+str(ufos), topleft=(20,20), color="skyblue")
    screen.draw.text(OBJECTIVE, midtop=(400,20), color="yellow", fontsize=40)
    screen.draw.text(message, midtop=(400,10), color="white")

    if game_over:
        screen.draw.text("GAME OVER", color="red", center=(400,350), fontsize=60)
        screen.draw.text("Try Again!", color="blue", center=(400,450),fontsize=30)
    elif game_complete:
        screen.draw.text("YOU WON", color="green", center=(400,350),fontsize=60)
        screen.draw.text("Good Job Soldier!", color="blue", center=(400,450),fontsize=30)
    
def place_UFO():
    ufo.x=randint(50,WIDTH-50)
    ufo.y=randint(50,HEIGHT-50)

def check_game_over():
    global game_over
    if lives==0:
        game_over=True

def check_game_complete():
    global game_complete
    if ufos<=0:
        game_complete=True

def on_mouse_down(pos):
    global ufos,message,lives
    if game_over or game_complete:
        return
    if ufo.collidepoint(pos):
        ufos-=1
        message="Good Aim!"
        check_game_complete()
        if not game_complete:
            place_UFO()
        else:
            ufo.x=10000000
            ufo.y=10000000
    else:
        lives-=1
        message="You Missed!"
        check_game_over()

place_UFO()
pgzrun.go()
