import turtle
import time
import random
bricksx=-350
score=0
life=3
highscore=0
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0
b8=0
b9=0
b0=0
yspeed=0
xspeed=0
win=turtle.Screen()
win.title("breakout")
win.bgcolor('Black')
win.setup(width=800, height=700)
win.tracer(0)
#Player
player=turtle.Turtle()
player.speed=0
player.shape("square")
player.color("white")
player.penup()
player.goto(0,-300)
player.shapesize(stretch_len=5, stretch_wid=1)
#Ball
ball=turtle.Turtle()
ball.speed(0.1)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.dx=-0.6
ball.dy=-0.6
#bricks
bricks=turtle.Turtle()
bricks.speed(0)
bricks.shape("square")
bricks.color("red")
bricks.penup()
bricks.shapesize(stretch_len=3.5, stretch_wid=0.75)
#bricks that make bricks dissapear
nobricks=turtle.Turtle()
nobricks.speed(0)
nobricks.shape("square")
nobricks.color("black")
nobricks.penup()
nobricks.shapesize(stretch_len=3.5, stretch_wid=0.75)
nobricks.goto(1000,1000)
#WriteScore
wscore = turtle.Turtle()
wscore.speed(0)
wscore.shape("square")
wscore.color("white")
wscore.penup()
wscore.hideturtle()
wscore.goto(0, 300)
wscore.write("Score: 0 High Score: 0", align="center", font=("Courier", 24,
"normal"))
lives = turtle.Turtle()
lives.speed(0)
lives.shape("square")
lives.color("white")
lives.penup()
lives.hideturtle()
lives.goto(0, 250)
lives.write("Lives: 3", align="center", font=("Courier", 24, "normal"))
#lives
for x in range(10):
     bricks.penup()
     bricks.goto(bricksx,100)
     bricksx=bricksx+77
     bricks.stamp()
#moving paddle
def playerleft():
     x=player.xcor()
     x-= 25
     player.setx(x)
def playerright():
     x=player.xcor()
     x+= 25
     player.setx(x)
#Keybinds
win.listen()
win.onkeypress(playerleft, "a")
win.listen()
win.onkeypress(playerright, "d")
while True:
 #block reset
    if b0>=1 and b1>=1 and b2>=1 and b3>=1 and b4>= 1and b5>=1 and b6>=1 and b7>=1 and b8>=1 and b9>=1:
        bricksx=-350
        for x in range(10):
            bricks.penup()
            bricks.goto(bricksx, 100)
            bricksx = bricksx + 77
            bricks.stamp()
        ball.dx=-1
        ball.dy=-1
        b0=0
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
 #score/brick colisions
    if b1<=0:
        if (100>ball.ycor()>90) and (-400 < ball.xcor() < -325):
            nobricks.goto(-350, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b1=1+b1
    if b2<=0:
        if (100>ball.ycor()>90) and (-325 < ball.xcor() < -212):
            nobricks.goto(-273, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b2=1+b2
    if b3<=0:
        if (100>ball.ycor()>90) and (-212 < ball.xcor() < -134):
            nobricks.goto(-196, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b3=b3+1
    if b4<=0:
        if (100>ball.ycor()>90) and (-134 < ball.xcor() < -20):
            nobricks.goto(-119, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b4=b4+1
    if b5<=0:
        if (100>ball.ycor()>90) and (-20 < ball.xcor() < 50):
            nobricks.goto(-42, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b5=b5+1
    if b6<=0:
        if (100>ball.ycor()>90) and (50 < ball.xcor() < 134):
            nobricks.goto(35, 100)
            nobricks.stamp()
            score=score+1
            ball.dy=-1
            b6=b6+1
    if b7<=0:
        if (100>ball.ycor() > 90) and (134 < ball.xcor() < 195):
            nobricks.goto(112, 100)
            nobricks.stamp()
            score = score + 1
            ball.dy = -1
            b7=b7+1
    if b8<=0:
        if (100>ball.ycor() > 90) and (189 < ball.xcor() < 266):
            nobricks.goto(189, 100)
            nobricks.stamp()
            score = score + 1
            ball.dy = -1
            b8=b8+1
    if b9<=0:
        if (100>ball.ycor() > 90) and (245 < ball.xcor() < 320):
            nobricks.goto(266, 100)
            nobricks.stamp()
            score = score + 1
            ball.dy = -1
            b9=b9+1
    if b0<=0:
        if (100>ball.ycor() > 90) and (320 < ball.xcor() < 420):
            nobricks.goto(343, 100)
            nobricks.stamp()
            score = score + 1
            ball.dy = -1
            b0=b0+1
 #Ball Move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
 #Collisions
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.ycor()<-350:
        ball.sety(0)
        ball.setx(0)
        life=life-1
        time.sleep(2)
        ball.dx=0.1
        ball.dy=0.1
    if ball.ycor()>340:
        ball.sety(340)
        ball.dy *= -1
    lives.clear()
    lives.write("Lives: {}".format(life), align="center", font=("Courier", 24,"normal"))
 #Collision code inspired by christian thompson
    if ball.ycor()<-300 and (player.xcor() + 50 > ball.xcor() > player.xcor() - 50):
        ball.dy *= -1
    wscore.clear()
    wscore.write("Score: {}".format(score), align="center", font=("Courier", 24,"normal"))
    win.update()
    if life<=0:
        bricksx=-350
        score=highscore
        for x in range(10):
            bricks.penup()
            bricks.goto(bricksx, 100)
            bricksx = bricksx + 77
            bricks.stamp()
    if life <=0:
        score=0
        life=3
win.mainloop
