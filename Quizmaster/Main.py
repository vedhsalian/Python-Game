import pgzrun

TITLE="Quiz Master"
WIDTH=870
HEIGHT=650

marque_box=Rect(0,0,880,80)
question_box=Rect(20,100,650,150)
timer_box=Rect(700,100,150,150)
answer_box1=Rect(20,270,300,150)
answer_box2=Rect(370,270,300,150)
answer_box3=Rect(20,450,300,150)
answer_box4=Rect(370,450,300,150)
skip_box=Rect(700,270,150,330)

score=0
time_left=10
question_file_name="Question.txt"
marque_message=""
is_game_over=False

answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0

def draw():
    global marque_message
    screen.clear()
    screen.fill("black")

    screen.draw.filled_rect(marque_box,"black")
    screen.draw.filled_rect(question_box,"lime")
    screen.draw.filled_rect(timer_box,"lightgreen")
    screen.draw.filled_rect(skip_box,"darkgreen")

    for answer in answer_boxes:
        screen.draw.filled_rect(answer,"olive")
    
    marque_message="Welcome to Quiz Master...."
    marque_message=marque_message+f"Q:{question_index} of {question_count}"

    screen.draw.textbox(marque_message,marque_box,color="white")
    screen.draw.textbox(str(time_left),timer_box, color="darkblue")
    screen.draw.textbox("Skip",skip_box,color="white",angle=-90)   

pgzrun.go()