import turtle


turtle.hideturtle()
turtle.pensize(10)



# Set speed to max
turtle.speed(0)

# Pen up, so it does not draw
turtle.pu()

# Make turtle go to the left edge of the screen
turtle.setx(-turtle.window_width()//2)

# Make the turtle go the bottom
turtle.sety(-turtle.window_height()//2)


# A function to draw the grid
def drawGrid():
    turtle.fd(turtle.window_width()//2)
    turtle.lt(90)
    turtle.fd(turtle.window_height()//2)
    turtle.lt(90)
    turtle.fd(turtle.window_width()//2)
    turtle.lt(90)
    turtle.fd(turtle.window_height()//2)
    turtle.lt(90)


# Pen down to draw the grid
turtle.pd()
drawGrid()


# A small function to reset to original position
def reSet():
    turtle.goto(0,0)
    turtle.pd()


turtle.pu()
reSet()
drawGrid()


def drawSquare():
    turtle.fd(turtle.window_width()//4)
    turtle.lt(90)
    turtle.fd(turtle.window_height()//4)
    turtle.lt(90)
    turtle.fd(turtle.window_width()//4)
    turtle.lt(90)
    turtle.fd(turtle.window_height()//4)
    turtle.lt(90)



# Make the turtle go to the left
turtle.setx(-turtle.window_width()//2)

# Make the turtle go the bottom
turtle.sety(-turtle.window_height()//2)





def move_turtle():
    turtle.pu()
    turtle.pd()
    while not (turtle.xcor() >= turtle.window_width()):
        drawSquare()
        turtle.setx(turtle.xcor() + (turtle.window_width()//4))



def make_box():
    boxes = 0
    while boxes != 4:
        move_turtle()
        turtle.setx(-turtle.window_width())
        turtle.sety(turtle.ycor() + (turtle.window_height() // 4))
        boxes +=1



turtle.pensize(1)
make_box()



turtle.pu()
turtle.goto(0,0)



'''
# Wrap this in a while loop
take_input = turtle.textinput('','Make a move')
make_move = turtle.write(take_input, move= False, align = 'left', font = ('Arial', 28,'normal'))
'''




########### filling in the boxes with the starting puzzle
'''
puzzle1 = [[3,4,1,3],[0,0,0,0],[0,0,0,0],[4,2,3,1]]
'''




turtle.done()

'''
def write_input():
    take_inputv2 = turtle.textinput('', 'Make a move')
    make_move = turtle.write(take_inputv2, move=False, align='left', font=('Arial', 45, 'normal'))
    return make_move


def append_board(user_input,puzzle):

    #Assumes the puzzle is a nested list
    #Appends the entry with users input


    for i in range(0, len(grid_rows)):
        if user_input[0] == grid_rows[i]:
            for j in range(0, len(grid_cols)):
                if user_input[1] == grid_cols[j]:
                    puzzle[i].insert(j, int(user_input))

'''