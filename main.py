import turtle
import time
import random

wn = turtle.Screen()
wn.title("Fuckets and Nubs")
wn.bgcolor("#8E5572")
wn.setup(width=800, height=600, startx=200)
wn.tracer(0)


score_a = 0
score_b = 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("#BBBE64")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.pu()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("#BBBE64")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.pu()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#F2F7F2")
ball.pu()
ball.goto(0, 0)


pen = turtle.Turtle()
pen.speed(0)
pen.color("#DFA06E")
pen.ht()
pen.pu()
pen.goto(0, 255)
pen.color("#F5F3BB")
pen.write(
    "Player A: 0  Player B: 0",
    align="center",
    font=(
        "Rustic_Jack",
        24,
        "normal",
    ),
)


def paddle1_up():
    y = paddle1.ycor()
    y += 10
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 10
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 10
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 10
    paddle2.sety(y)


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
# wn.onkey(paddle2_up, "Up")
# wn.onkey(paddle2_down, "Down")

ball.dx = 0.05
ball.dy = 0.05
ball.di = 0.005

running = True
game_time = 0

ps = 50


while running == True:

    # player 2 ai
    if ball.xcor() > -50:
        if ball.ycor() > (paddle2.ycor()):
            paddle2_up()
        elif ball.ycor() < (paddle2.ycor()):
            paddle2_down()

    # player 1 ai
    if ball.ycor() > (paddle1.ycor() + ps):
        paddle1_up()
    elif ball.ycor() < (paddle1.ycor() - ps):
        paddle1_down()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    wn.update()

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_a, score_b),
            align="center",
            font=("Rustic_Jack", 24, "normal"),
        )
        # speed up ball after point won
        if ball.dx > 0:
            ball.dx += ball.di
        else:
            ball.dx -= ball.di

        if ball.dy > 0:
            ball.dy += ball.di
        else:
            ball.dy -= ball.di

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_a, score_b),
            align="center",
            font=("Rustic_Jack", 24, "normal"),
        )
        # speed up ball after point won
        if ball.dx > 0:
            ball.dx += ball.di
        else:
            ball.dx -= ball.di

        if ball.dy > 0:
            ball.dy += ball.di
        else:
            ball.dy -= ball.di

    if (
        (ball.xcor() > 340 and ball.xcor() < 350)
        and ball.ycor() < paddle2.ycor() + 50
        and ball.ycor() > paddle2.ycor() - 50
    ):
        ball.setx(340)
        ball.dx *= -1

    if (
        (ball.xcor() < -340 and ball.xcor() > -350)
        and ball.ycor() < paddle1.ycor() + 50
        and ball.ycor() > paddle1.ycor() - 50
    ):
        ball.setx(-340)
        ball.dx *= -1

    if paddle1.ycor() > 240:
        paddle1.sety(240)

    if paddle1.ycor() < -240:
        paddle1.sety(-240)

    if paddle2.ycor() > 240:
        paddle2.sety(240)

    if paddle2.ycor() < -240:
        paddle2.sety(-240)

    max_score = 10

    if score_a == max_score or score_b == max_score:
        running = False

paddle1.hideturtle()
paddle2.hideturtle()
ball.hideturtle()
wn.update()
pen.clear()
pen.goto(0, 0)

if score_a > score_b:
    pen.write("You Win!", align="center", font=("Timeline", 40, "normal"))
else:
    pen.write("You Lose!", align="center", font=("Timeline", 40, "normal"))


time.sleep(5)
exit(0)
