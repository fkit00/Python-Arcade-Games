from turtle import Screen, Turtle 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Welcome to Pong!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0) # this combined with update stops the animation moving to place

ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        print('made contact')
        ball.bounce_x()


# we want to detetc collision with paddles


screen.exitonclick()
