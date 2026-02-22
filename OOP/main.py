"""
oop - Object Oriented Programming

oop -- 1)class
       2)objects

class-- blueprint of an element - ball
object-- instance of a class -- red ball, blue ball, green ball

objects -- 1)attributes - colors, size
           2)methods - move, burst

"""
import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("OOP")

FPS=60
clock=pygame.time.Clock()

class Rect():
    def __init__(self,color,dimensions):
        self.rect_surf=screen
        self.rect_color=color
        self.rect_dimensions=dimensions

    def draw(self):
        self.draw_rect=pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimensions)

    def move(self):
        self.rect_dimensions

greenRect=Rect("green",(50,20,100,120))
hotpinkRect=Rect("hotpink",(150,120,100,120))
OrangeRect=Rect("orange",(250,220,100,120))
DarkblueRect=Rect("darkblue",(350,320,100,120))
CyanRect=Rect("cyan",(450,420,100,120))

gameloop=True
while gameloop:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            gameloop=False
    
    screen.fill("black")


    greenRect.draw()
    hotpinkRect.draw()
    OrangeRect.draw()
    DarkblueRect.draw()
    CyanRect.draw()
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()