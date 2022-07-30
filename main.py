import turtle as t
import random
import colorgram

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def image_color():
    random_image_color = random.choice(colors)
    # print(random_image_color.rgb.r, random_image_color.rgb.g, random_image_color.rgb.b)
    return random_image_color.rgb.r, random_image_color.rgb.g, random_image_color.rgb.b


def draw_dot(space, x):
    """Space between dots, x is for how many dots per loop"""

    t.penup()
    t.setpos(-400, 400)
    t.speed("fastest")
    t.hideturtle()
    for i in range(x):
        # t.color(random_color())
        for j in range(x):
            t.color(image_color())
            t.pensize(10)
            t.dot()

            t.forward(space)
        t.backward(space * x)

        t.right(90)
        t.forward(space)
        t.left(90)


colors = colorgram.extract("image.jpg", 6)

image_color()

t.screensize(bg="black")
draw_dot(50, 10)

screen = t.Screen()

t.exitonclick()
