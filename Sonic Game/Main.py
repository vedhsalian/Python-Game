import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=500

number_of_sonics=8
sonics=[]
lines=[]
next_sonic=0
total_time=0
end_time=0
start_time=0

def draw_sonic():
    global start_time
    for i in range(number_of_sonics):
        sonic=Actor('sonic')
        sonic.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        sonics.append(sonic)
    start_time=time()

def draw():
    global total_time,start_time
    number=1
    screen.blit('greenhills',(0,0))

    for sonic in sonics:
        screen.draw.text(str(number), (sonic.pos[0]-50,sonic.pos[1]-40))

        sonic.draw()
        number+=1
    
    for line in lines:
        screen.draw.line(line[0],line[1], (255,255,255))
    
    if next_sonic<number_of_sonics:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=20,color="white")
    else:
        screen.fill("black")
        screen.draw.text(str(round(total_time,1)),center=(400,250),fontsize=80,color="white")

def update():
    pass

def on_mouse_down(pos):
    global next_sonic,lines
    if next_sonic<number_of_sonics:
        if sonics[next_sonic].collidepoint(pos):
            if next_sonic:
                lines.append((sonics[next_sonic-1].pos,sonics[next_sonic].pos))
            next_sonic+=1
        else:
            lines=[]
            next_sonic=0

draw_sonic()
pgzrun.go()