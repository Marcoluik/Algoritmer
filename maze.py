import turtle
import random
turtle.setup(800, 800)
turtle.bgcolor("black")
width = 5
length = 80
cols = 10
rows = 10
base_x = -400
base_y = -400
color_lst = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "pink"]
turtle.pensize(width)
turtle.pencolor("white")
turtle.speed(0)
turtle.penup()
turtle.sety(base_y)
turtle.setx(base_x)
turtle.pendown()

def draw_maze():
    for i in range(cols):
        x = -400+i*length
        turtle.penup()
        for j in range(rows):
            turtle.pencolor()
            y=-400+j*length
            new_x = x + length
            turtle.goto(x, y)
            turtle.pendown()
            direction = random.randrange(1,5)
            color = random.randrange(len(color_lst))
            turtle.pencolor(color_lst[color])

            if direction == 1:
                turtle.goto(new_x, y)
            elif direction == 2:
                turtle.goto(new_x, y+length)
            elif direction == 3:
                turtle.goto(new_x, y-length)
            elif direction == 4:
                turtle.goto(x, y+length)
            turtle.penup()

draw_maze()
turtle.done()