import pgzrun

from random import randint

#constants to set the width and the height of the root window

WIDTH=300

HEIGHT =300

#this is a built in function that helps you to display elements on the screen def draw):
def draw():
    screen. fill("black")

    r=255

    g=0

    b=randint (120, 255)

    width=WIDTH

    height=HEIGHT-200

    for i in range(20):

        rect=Rect ((0,0), (width, height))

        rect.center=150,150
        screen.draw.rect(rect, (r,g,b))

        r-=10

        g+=10

        width -=10

        height +=10

#to keep it constant
pgzrun.go()