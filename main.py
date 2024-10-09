import time
from turtle import Turtle, Screen
from paddle import Paddle
from score import Score

score = Score()
from ball import Ball
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball((0,0))

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
positions = [(0,-270),(0,-240), (0,-210), (0,-180), (0,-150), (0,-120), (0,-90), (0,-60), (0,-30), (0,0), (0,30), (0,60), (0,90), (0,120), (0, 150), (0,180), (0,210),(0,240), (0,270)]
screen.tracer(0)
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")






game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 270 or ball.ycor()< -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        score.increase_l_score()
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        score.increase_r_score()
        ball.bounce_x()






screen.exitonclick()
