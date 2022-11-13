import random
import time
import turtle

# ? Canvas settings
wn = turtle.Screen()
wn.title("Attemt numbah 2")
wn.bgcolor("#8E5572")
wn.setup(width=800, height=600, startx=200)
wn.tracer(0)

# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("#BBBE64")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.pu()
paddle1.goto(-350, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("#BBBE64")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.pu()
paddle2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#F2F7F2")
ball.pu()
ball.goto(0, 0)

# net
net = turtle.Turtle()
net.speed(0)
net.fillcolor("black")
net.begin_fill()
net.pu()
net.goto(140, 300)
net.right(90)
net.pendown()
net.goto(140, -300)
net.hideturtle()


# scoreboard
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


# ? paddle movement functions
def paddle1_up():
    if paddle1.ycor() > 240:
        pass
    else:
        y = paddle1.ycor()
        y += 10
        paddle1.sety(y)


def paddle1_down():
    if paddle1.ycor() < -240:
        pass
    else:
        y = paddle1.ycor()
        y -= 10
        paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 3
    paddle2.sety(y)
    paddle2.color("red")


def paddle2_down():
    y = paddle2.ycor()
    y -= 3
    paddle2.sety(y)
    paddle2.color("red")


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")


# Ball Delta
ball.dx = 3
ball.dy = 3

score_a = 0
score_b = 0
max_score = 10
running = True
fps = 60

# ? cpu ai


def ai():
    if ball.xcor() > 140 and ball.dx > 0:
        if ball.ycor() > (paddle2.ycor() + 50):
            paddle2_up()
        elif ball.ycor() < (paddle2.ycor() - 50):
            paddle2_down()


# ? ball movement


def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# ? check collisions
def check_bounce():
    global score_a
    global score_b
    # check ceiling/floor bounces
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # check goal scored
    if ball.xcor() > 390:
        score_a += 1
        point_won()

    if ball.xcor() < -390:
        score_b += 1
        point_won()

    # check paddle collision
    if (
        (ball.xcor() > 340 and ball.xcor() < 350)
        and ball.ycor() < paddle2.ycor() + 55
        and ball.ycor() > paddle2.ycor() - 55
    ):
        paddle2.color("black")
        ball.dx *= -1
        ball.setx(340)
        if ball.ycor() > paddle2.ycor():
            ball.dy += 0.5
        else:
            ball.dy -= 0.5

        print(f"ball delta ({ball.dx}, {ball.dy}")

    if (
        (ball.xcor() < -340 and ball.xcor() > -350)
        and ball.ycor() < paddle1.ycor() + 55
        and ball.ycor() > paddle1.ycor() - 55
    ):
        ball.setx(-340)
        ball.dx *= -1

        if ball.ycor() > paddle1.ycor():
            ball.dy += 0.1
        else:
            ball.dy -= 0.1
        print(f"ball delta ({ball.dx}, {ball.dy}")


# check clipping

# ? point won


def point_won():
    global running
    global score_a
    global score_b
    paddle2.color("black")
    # update ball direction
    ball.goto(0, 0)
    ball.dx *= -1
    # update score (pen)
    pen.clear()
    pen.write(
        "Player A: {}  Player B: {}".format(score_a, score_b),
        align="center",
        font=("Rustic_Jack", 24, "normal"),
    )
    ball.dx += 0.1
    ball.dy = ball.dx
    print(f"ball delta = ({ball.dx},{ball.dy})")

    # check if game is won
    if score_a == max_score or score_b == max_score:
        running = False


# ? endgame
def game_over():

    # clear screen
    paddle1.hideturtle()
    paddle2.hideturtle()
    ball.hideturtle()
    wn.update()
    pen.clear()
    pen.write(
        "Player A: {}  Player B: {}".format(score_a, score_b),
        align="center",
        font=("Rustic_Jack", 24, "normal"),
    )
    pen.goto(0, -50)

    # display score and winner
    if score_a > score_b:
        pen.write("You Win!", align="center", font=("Timeline", 40, "normal"))
    else:
        pen.write("You Lose!", align="center", font=("Timeline", 40, "normal"))

    time.sleep(5)
    exit(0)


# ? main gameplay
def mainloop(fps):

    frame_dur = 1 / fps

    while running:
        start = time.time()
        move_ball()
        ai()
        check_bounce()
        wn.update()
        lag = time.time() - start  # how much time it took to run game loop
        sleep = frame_dur - lag

        if sleep > 0:
            time.sleep(sleep)
            # print(sleep)


mainloop(fps)

game_over()
