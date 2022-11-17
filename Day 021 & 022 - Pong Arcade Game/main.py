# 1. create the screen - done
# 2. create and move a paddle - done
# 3. create another paddle - done
# 4. create the ball and make it move - done
# 5. detect collosion with wall and bounce - done
# 6. detect collison with paddle - done
# 7. detetct when paddle misses - done
# 8. keep score - done

#importing classes
from turtle import Turtle,Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

#setting up screen
screen=Screen()
screen.setup(width=1000,height=1000)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#setting up pong paddles+ball+score
paddle=Paddle()
ball=Ball()
score=Score()

#setting up user commands
screen.listen()
screen.onkey(paddle.user_up,"Up")
screen.onkey(paddle.user_down,"Down")
screen.onkey(paddle.pc_up,"w")
screen.onkey(paddle.pc_down,"s")

game_is_on=True
n=0.2

#setting ball movements and collisions

while game_is_on:
    screen.update()
    time.sleep(n)
    ball.move()
#checking hit with paddle_user
    if paddle.paddle_user.distance(ball)<50:
        if ball.xcor()>450:
            n/=2 #increasing speed
            score.increase_user() #increasing score
            ball.bounce_paddle()

#checking hit with paddle_pc
    elif paddle.paddle_pc.distance(ball)<30:
        if ball.xcor()>-450:
            n/=2 #increasing speed
            score.increase_pc() #increasing score
            ball.bounce_paddle()

#checking hit with ball to bounce back
    elif ball.ycor()>480 or ball.ycor()<-480:
        ball.bounce_wall()

#checking for game over
    elif ball.xcor()>480 or ball.xcor()<-480:
        score.game_over()
        game_is_on=False

screen.exitonclick()