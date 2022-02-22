from time import sleep
from turtle import *
import random


screen = Screen()       #object of Screen class
screen.setup(width=600, height=600)
screen.title("Snake")   #game title
screen.bgcolor("black") #background color
screen.tracer(False) #to slow the animation

initial_speed = 0.1
max_speed = 0.02
game_speed = initial_speed

score = 0
score_text = Turtle()
score_text.penup()
score_text.goto(-250,270)
score_text.color("red")
score_text.write("Score:"+str(score),font=('Bradley Hand ITC', 20),align='center')
score_text.hideturtle()

high_score = 0
high_score_text = Turtle()
high_score_text.penup()
high_score_text.goto(-80,270)
high_score_text.color("green")
high_score_text.write("High Score:"+str(high_score),font=('Bradley Hand ITC', 20),align='center')
high_score_text.hideturtle()


snake_head = Turtle()
snake_head.shape("square")
snake_head.penup()
snake_head.color("white")
snake_head.goto(0,0)
snake_head.direction='up'

snake_body = []
snake_body.append(snake_head)

food = Turtle()
food.shape("circle")
food.shapesize(.8)
food.penup()
food.color("white")
food.goto(100,10)

def move_up():
    if snake_head.direction != 'down': 
        snake_head.direction='up'

def move_down():
    if snake_head.direction != 'up':
        snake_head.direction='down'

def move_right():
    if snake_head.direction != 'left':
        snake_head.direction='right'

def move_left():
    if snake_head.direction != 'right':
        snake_head.direction='left'


def snake_movement():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        y = y + 15
        snake_head.sety(y)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        y = y - 15
        snake_head.sety(y)    
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        x = x + 15
        snake_head.setx(x)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        x = x - 15
        snake_head.setx(x)    

def food_eaten():
    if snake_head.distance(food) < 15:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x, y)
        
        body = Turtle()
        body.shape("square")
        body.shapesize(.9)
        body.penup()
        body.color("white")
        body.hideturtle()
        global snake_body
        snake_body.append(body)
        
        global score
        score = score + 1
        score_text.clear()
        score_text.write("Score:"+str(score),font=('Bradley Hand ITC', 20),align='center')

        game_difficulty()

def game_difficulty():
    global game_speed
    global max_speed
    global score
    decrement = 0.01 * initial_speed
    if game_speed - decrement != max_speed:
        game_speed = game_speed - decrement

def boarders_exceed():
    if snake_head.xcor() > 299 or snake_head.xcor() < -299 :
        reset_game()
        # x = snake_head.xcor() * -1
        # y = snake_head.ycor()
        # snake_head.goto(x,y)
    if snake_head.ycor() > 299 or snake_head.ycor() < -299 :
        reset_game()
        # x = snake_head.xcor()
        # y = snake_head.ycor() * -1
        # snake_head.goto(x,y)

def reset_game():
    global snake_body
    for i in range(len(snake_body)-1,1,-1):
        snake_body[i].hideturtle()
        del snake_body[i]
    
    high_score_check()
    global score
    score = 0
    score_text.clear()
    score_text.write("Score:"+str(score),font=('Bradley Hand ITC', 20),align='center')
    snake_head.goto(0,0)
    snake_head.direction = 'stop'
    
    global initial_speed
    global game_speed
    game_speed = initial_speed

def body_hit():
        if(len(snake_body) >= 4 ):
            for i in range(len(snake_body)-1,3,-1):
                if snake_body[i].distance(snake_head) < 10:
                    reset_game()
                    break

def high_score_check():
    global score
    global high_score
    if score > high_score:
        high_score = score
        high_score_text.clear()
        high_score_text.write("High Score:" + str(high_score),font=('Bradley Hand ITC', 20),align='center')

screen.listen()
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')
screen.onkeypress(move_right,'Right')
screen.onkeypress(move_left,'Left')




while True:
    screen.update()        
    snake_movement()
    sleep(game_speed)

    print(game_speed)
    food_eaten()
    boarders_exceed()
    body_hit()
    print("speed: "+str(game_speed)+" speedperce: " + str((((initial_speed - max_speed) - (game_speed - max_speed))/(initial_speed - max_speed))*100 )+"%")
    
    #body movement
    if(len(snake_body) != 0):
        for i in range(len(snake_body)-1,0,-1):
            x = snake_body[i-1].xcor()
            y = snake_body[i-1].ycor()
            snake_body[i].showturtle()
            snake_body[i].goto(x,y)