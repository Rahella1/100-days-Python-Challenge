import random
from turtle import Turtle, Screen
import turtle as t
# tim = t.Turtle()
tim = Turtle()
t.colormode(255)

# how to make the turtle move to random location
tim.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    color = (r, g, b)
    return color
# tim.shape("turtle")
# tim.color("springGreen")
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# for i in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.speed(9)

#Drwaing Sphirograph

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        #tim.speed(9)


draw_spirograph(5)

# tim.shape("turtle")
# tim.color("springGreen")

#Drawing a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

#Drawing different sides of shape
# colours = ["dark red", "magenta", "forest green", "goldenrod", "blue", "yellow", "medium slate blue",]
# def draw_shape(num_sides):
#     for i in range(num_sides):
#         angle = 360/num_sides
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     #tim.speed(9)
#     draw_shape(shape_side_n)

# import heroes
# print(heroes.gen())

#Drawing dotted lines
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()















screen = Screen()
screen.exitonclick()