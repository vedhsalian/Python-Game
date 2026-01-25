import pgzrun
import random

WIDTH=800

HEIGHT=600

CENTER_X=WIDTH/2

CENTER_Y=HEIGHT/2

FINAL_LEVEL=6

START_SPEED=10

Items=["battery","sodacan","plasticbag","chipspack"]

game_over=False

game_complete=False

current_level=1

items=[]

animations=[]

def draw():
    global items,game_over,game_complete,current_level

    screen.clear()

    screen.blit("recycle",(0,0))

    if game_over:
        screen.draw.text("GAME OVER",fontsize=60,center=(CENTER_X,CENTER_Y),color="red")
        screen.draw.text("Try again",fontsize=30,center=(400,350),color="blue")
    elif game_complete:
        screen.draw.text("YOU WON!!!",fontsize=60,color="green",center=(CENTER_X,CENTER_Y))
        screen.draw.text("Congrats, you did it!",fontsize=30,color="blue",center=(450,350))
    else:
        for item in items:
            item.draw()
            
def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def make_items(extra_items):
    items_to_create=get_option_to_create(extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(extra_items):
    items_to_create=["paperbag"]
    for i in range(0,extra_items):
        random_option=random.choice(Items)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_options=[]
    for i in items_to_create:
        item=Actor(i)
        new_options.append(item)
    return new_options

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size
        item.x=new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration=START_SPEED-current_level
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=check_game_over(),y=HEIGHT)
        animations.append(animation)
    

def check_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                check_game_complete()
            else:
                check_game_over()

def check_game_complete():
    global current_level,items,animations,game_complete
    stop_animations(animations)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text,subheading_text):
    screen.draw.text(heading_text, fontsize=40, center=(400,10), color="green")
    screen.draw.text(subheading_text, fontsize=20, center=(400,30), color="yellow")

pgzrun.go()
