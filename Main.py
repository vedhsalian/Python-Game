import pgzrun
from random import randint

TITLE="GOOD SHOT"

WIDTH=500
HEIGHT=500

message=""

target=Actor('target')

def draw():
    screen.clear()
    screen.fill("black")
    target.draw()
    screen.draw.text(message,center=(400,10), fontsize=30)

def place_target():
    target.x=randint(50,WIDTH-50)
    target.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if target.collidepoint(pos):
        message="Good Shot"
        place_target()
    else:
        message="You Missed"


place_target()
pgzrun.go()