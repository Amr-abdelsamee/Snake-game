from time import sleep
from turtle import *
import random


screen = Screen()       #object of Screen class
screen.setup(width=600, height=600)
screen.title("Snake")   #game title
screen.bgcolor("black") #background color
screen.tracer(False) #to slow the animation

score = 0
score_text = Turtle()
score_text.penup()
score_text.goto(-250,270)
score_text.color("red")
score_text.write("Score:"+str(score),font=('Bradley Hand ITC', 20),align='center')
score_text.hideturtle()


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
        y = y + 10
        snake_head.sety(y)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        y = y - 10
        snake_head.sety(y)    
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        x = x + 10
        snake_head.setx(x)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        x = x - 10
        snake_head.setx(x)    

def food_eaten():
    if snake_head.distance(food) < 10:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x, y)
        
        body = Turtle()
        body.shape("square")
        body.shapesize(0.9)
        body.penup()
        body.color("white")
        snake_body.append(body)
        
        global score
        score = score + 1
        score_text.clear()
        score_text.write("Score:"+str(score),font=('Bradley Hand ITC', 20),align='center')

def boarders_exceed():
    if snake_head.xcor() > 299 or snake_head.xcor() < -299 :
        x = snake_head.xcor() * -1
        y = snake_head.ycor()
        snake_head.goto(x,y)
    if snake_head.ycor() > 299 or snake_head.ycor() < -299 :
        x = snake_head.xcor()
        y = snake_head.ycor()* -1
        snake_head.goto(x,y)



screen.listen()
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')
screen.onkeypress(move_right,'Right')
screen.onkeypress(move_left,'Left')

while True:
    screen.update()        
    snake_movement()
    sleep(0.1)
    food_eaten()
    boarders_exceed()
    for i in range(len(snake_body)-1,0,-1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x,y)
