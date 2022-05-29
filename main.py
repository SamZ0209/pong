# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle

wn = turtle.Screen()
wn.title = "pong"
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B

pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(340, 0)


# function a
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    x = pad_b.ycor()
    x += 20
    pad_b.sety(x)


def pad_b_down():
    x = pad_b.ycor()
    x -= 20
    pad_b.sety(x)


# keyboard lining

wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(-5, 0)
ball.dx = .2
ball.dy = .2

# Score
Score_a = 0
Score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {},  Player B: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, "normal"))

# Main Game Loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(-5, 0)
        ball.dx = .2
        ball.dx *= -1
        Score_a += 1
        pen.clear()
        pen.write("Player A: {},  Player B: {}".format(Score_a, Score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(-5, 0)
        ball.dx = .2
        ball.dx *= -1
        Score_b += 1
        pen.clear()
        pen.write("Player A: {},  Player B: {}".format(Score_a, Score_b), align="center",
                  font=("Courier", 24, "normal"))

    # collision
    if (320 < ball.xcor() < 330) and (pad_b.ycor() + 40 > ball.ycor() > pad_b.ycor() - 40):
        ball.setx(320)
        ball.dx *= -1
        if ball.dx >= 0:
            ball.dx += .05
        else:
            ball.dx += -.05

    if (-340 < ball.xcor() < -330) and (pad_a.ycor() + 40 > ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
        if ball.dx >= 0:
            ball.dx += .05
        else:
            ball.dx += -.05

    # wall

    if pad_b.ycor() > 260:
        pad_b.sety(260)

    if pad_b.ycor() < -240:
        pad_b.sety(-240)

    if pad_a.ycor() > 260:
        pad_a.sety(260)

    if pad_a.ycor() < -240:
        pad_a.sety(-240)
