import turtle

wn = turtle.Screen()
wn.title('Fuckets and Nubs')
wn.bgcolor('#8E5572')
wn.setup(800, 600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('#BBBE64')
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.pu()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('#BBBE64')
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.pu()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('#F2F7F2')
ball.pu()
ball.goto(0, 0)

ball.dx = .25
ball.dy = .25

pen = turtle.Turtle()
pen.speed(0)
pen.color('#BCAA99')
pen.ht()
pen.pu()
pen.goto(0, 255)
pen.write('Player A: 0  Player B: 0', align='center', font=('Rustic_Jack', 24, 'normal'))

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)
    
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
    
wn.listen()
wn.onkeypress(paddle1_up, 'w')
wn.onkeypress(paddle1_down, 's')
wn.onkeypress(paddle2_up, 'Up')
wn.onkeypress(paddle2_down, 'Down')

while True:
    wn.update()
    
    if score_a or score_b <= 10:
        for i in range(0, 20):
            ball.dx = .25 * 2
            ball.dy = .25 * 2
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
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
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Rustic_Jack', 24, 'normal'))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Rustic_Jack', 24, 'normal'))
        
    if (
        (ball.xcor() > 340 and ball.xcor() < 350) 
        and ball.ycor() < paddle2.ycor() + 40 
        and ball.ycor() > paddle2.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1
        
    if (
        (ball.xcor() < -340 and ball.xcor() > -350) 
        and ball.ycor() < paddle1.ycor() + 40 
        and ball.ycor() > paddle1.ycor() - 40
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
        
    if score_a == 10:
        paddle1.ht()
        paddle2.ht()
        pen.clear()
        ball.ht()
        pen.goto(0, 0)
        pen.write('Player A Wins!', align='center', font=('Timeline', 40, 'normal'))
        
    if score_b == 10:
        paddle1.ht()
        paddle2.ht()
        pen.clear()
        ball.ht()
        pen.goto(0, 0)
        pen.write('Player B Wins!', align='center', font=('Timeline', 40, 'normal'))
        
    