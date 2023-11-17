import turtle
turtle.speed(0)
turtle.colormode(255)
rows = 17    #længde
cols = 4     #Bredte
turtle.bgcolor("black")
for j in range(rows):
    if j < 5:
        turtle.left(20)
    elif j > 5 and j < 10:
        turtle.left(-20)
    else:
        turtle.left(20)
    turtle.color(((j*10)+50,200,j*10))
    for i in range(cols):
        turtle.circle(10+(i*5), 180)
turtle.penup()
turtle.setpos(250,250)
turtle.pendown()
turtle.circle(30)
turtle.penup()

turtle.setpos(50,250)
turtle.pendown()
turtle.circle(30)
turtle.done()

