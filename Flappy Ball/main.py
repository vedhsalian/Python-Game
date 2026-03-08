import pgzrun
from random import randint

TITLE="Flappy Ball"
WIDTH=800
HEIGHT=600

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
    
    def draw(self):
        pos=(self.x,self.y)
        R=randint(0,255)
        G=randint(0,255)
        B=randint(0,255)
        CLR=(R,G,B)
        screen.draw.filled_circle(pos,self.radius,CLR)

ball1=Ball(400,300)
ball2=Ball(50,50)
ball3=Ball(750,50)
ball4=Ball(50,550)
ball5=Ball(750,550)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()

gravity=2000

def update(dt):
    uy=ball1.vy
    ball1.vy=ball1.vy+gravity*dt
    ball1.y=ball1.y+(uy+ball1.vy)*0.5*dt
    if ball1.y>HEIGHT-ball1.radius:
        ball1.y=HEIGHT-ball1.radius
        ball1.vy=-ball1.vy*0.9
    ball1.x=ball1.x+ball1.vx*dt
    if ball1.x>WIDTH-ball1.radius or ball1.x<ball1.radius:
        ball1.vx=-ball1.vx
    
    uy=ball2.vy
    ball2.vy=ball2.vy+gravity*dt
    ball2.y=ball2.y+(uy+ball2.vy)*0.5*dt
    if ball2.y>HEIGHT-ball2.radius:
        ball2.y=HEIGHT-ball2.radius
        ball2.vy=-ball2.vy*0.9
    ball2.x=ball2.x+ball2.vx*dt
    if ball2.x>WIDTH-ball2.radius or ball2.x<ball2.radius:
        ball2.vx=-ball2.vx
    
    uy=ball3.vy
    ball3.vy=ball3.vy+gravity*dt
    ball3.y=ball3.y+(uy+ball3.vy)*0.5*dt
    if ball3.y>HEIGHT-ball3.radius:
        ball3.y=HEIGHT-ball3.radius
        ball3.vy=-ball3.vy*0.9
    ball3.x=ball3.x+ball3.vx*dt
    if ball3.x>WIDTH-ball3.radius or ball3.x<ball3.radius:
        ball3.vx=-ball3.vx

    uy=ball4.vy
    ball4.vy=ball4.vy+gravity*dt
    ball4.y=ball4.y+(uy+ball4.vy)*0.5*dt
    if ball4.y>HEIGHT-ball4.radius:
        ball4.y=HEIGHT-ball4.radius
        ball4.vy=-ball4.vy*0.9
    ball4.x=ball4.x+ball4.vx*dt
    if ball4.x>WIDTH-ball4.radius or ball4.x<ball4.radius:
        ball4.vx=-ball4.vx
    
    uy=ball5.vy
    ball5.vy=ball5.vy+gravity*dt
    ball5.y=ball5.y+(uy+ball5.vy)*0.5*dt
    if ball5.y>HEIGHT-ball5.radius:
        ball5.y=HEIGHT-ball5.radius
        ball5.vy=-ball5.vy*0.9
    ball5.x=ball5.x+ball5.vx*dt
    if ball5.x>WIDTH-ball5.radius or ball5.x<ball5.radius:
        ball5.vx=-ball5.vx

def on_key_down(key):
    if key==keys.SPACE:
        ball1.vy=-500
    
    if key==keys.UP:
        ball2.vy=-500

    if key==keys.C:
        ball3.vy=-500

    if key==keys.V:
        ball4.vy=-500

    if key==keys.B:
        ball5.vy=-500

pgzrun.go()