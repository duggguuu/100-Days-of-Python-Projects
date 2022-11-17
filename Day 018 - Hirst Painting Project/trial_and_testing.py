from turtle import Screen
import turtle as t
import random
screen=Screen()
tim = t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple

tim.pensize(1)
tim.speed("fastest")

def draw_spiral(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spiral(1)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# tim.pensize(10)
# tim.speed(50)

# direction = ["forward","backward"]
# turns = ["left","right"]

# for _ in range (100):
#     tim.color(random_color())
#     move=random.choice(direction)
#     if move=="forward":
#      tim.forward(20)
#     elif move=="backward":
#      tim.backward(20)
#     turn=random.choice(turns)
#     if turn=="left":
#      tim.left(90)
#     elif turn=="right":
#      tim.right(90)





screen.exitonclick()