from time import sleep
from turtle import *


screen = Screen()       #object of Screen class
screen.setup(width=600, height=600)
screen.title("Snake")   #game title
screen.bgcolor("black") #background color
screen.tracer(False) #to slow the animation


# text_bar = Turtle()
# text_bar.shape("square")
# text_bar.penup()
# text_bar.color("white")
# text_bar.goto(-300,300)
# text_bar.shapesize(2,60)

score_text = Turtle()
score_text.penup()
score_text.goto(-250,270)
score_text.color("red")
score_text.write("Score:0",font=('Bradley Hand ITC', 20),align='center')
score_text.hideturtle()


snake_head = Turtle()
snake_head.shape("square")
snake_head.penup()
snake_head.color("white")
snake_head.goto(0,0)
snake_head.direction='up'


food = Turtle()
food.shape("circle")
food.shapesize(.8)
food.penup()
food.color("white")
food.goto(100,10)

def move_up():
    snake_head.direction='up'
def move_down():
    snake_head.direction='down'
def move_right():
    snake_head.direction='right'
def move_left():
    snake_head.direction='left'

screen.listen()
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')
screen.onkeypress(move_right,'Right')
screen.onkeypress(move_left,'Left')


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

while True:
    screen.update()        
    snake_movement()
    sleep(0.1)

