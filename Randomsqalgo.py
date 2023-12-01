import turtle
import random
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "white"]
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
turtle.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
turtle.bgcolor("black")
turtle.title("Kvadrat")
turtle.speed(0)
max = 4

def split_or_fill(x,y,width,stage,max_stage):
    if stage <= max_stage: #Hvis stage er mindre end Max
        fill = random.random()

        if fill < 0.5 and stage > 0 or stage == max_stage and stage > 0: #10% chance
            tegn_kvadrat(x,y,random.choice(colors),width)
        else:
            number_of_cols = random.randrange(2,4)
            for række in range(number_of_cols):
                for søjle in range(number_of_cols):
                    split_or_fill(x+søjle*width/number_of_cols,
                                  y+række*width/number_of_cols,
                                  width/number_of_cols,
                                  stage+1,
                                  max_stage)




def tegn_kvadrat(x,y,col,length):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.fillcolor(col)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

split_or_fill((-SCREEN_WIDTH/2),(-SCREEN_WIDTH/2),SCREEN_WIDTH,0,4)

turtle.done()
