import pgzrun
from random import randint

TITLE="GOOD SHOT"

WIDTH=500
HEIGHT=500

message=""

alien=Actor('alien')

def draw():
    screen.clear()
    screen.fill("black")
    alien.draw()
    screen.draw.text(message,center=(400,10), fontsize=30)

def place_alien():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good Shot"
        place_alien()
    else:
        message="You Missed"


place_alien()
pgzrun.go()