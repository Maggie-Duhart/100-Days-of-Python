# import colorgram
#
# rgb_colors = []
# # Extract 30 colors from an image
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Screen
import turtle as t
import random

t.colormode(255)

color_list = [(58, 105, 148), (222, 234, 229), (225, 202, 110), (133, 85, 57), (220, 147, 74), (231, 224, 203),
              (143, 178, 201), (195, 145, 171), (235, 221, 231), (141, 78, 102), (212, 90, 65), (135, 181, 137),
              (64, 109, 91), (188, 82, 119), (151, 134, 66), (64, 157, 95), (43, 156, 190), (183, 191, 202),
              (216, 176, 191), (108, 121, 157), (7, 58, 104), (13, 68, 123), (156, 28, 38), (231, 174, 163),
              (173, 202, 183), (158, 203, 215), (174, 24, 17), (73, 57, 40), (78, 65, 46)]

t.speed("fastest")
t.penup()
t.hideturtle()
t.goto(-300, -300)


def go_back():
    t.right(180)
    t.penup()
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)


drawing = True

while drawing:
    for row in range(0, 10):
        for _ in range(10):
            t.color(random.choice(color_list))
            t.dot(20)
            t.forward(50)

        go_back()
    drawing = False

screen = Screen()
screen.exitonclick()
