import turtle as turtle_module
import random
import colorgram

tim = turtle_module.Turtle()
tim.speed("fastest")
# tim.penup()
# tim.hideturtle()

screen=turtle_module.Screen()

turtle_module.colormode(255)
colors=colorgram.extract('hirst_painting.jpg',30)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
color_list=rgb_colors

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()