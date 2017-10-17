import turtle
turtle.showturtle()

turtle.pu()
turtle.pensize(10)


'''
def row_A():
    turtle.sety(turtle.window_height() // 1.5)
    return turtle.ycor()

def row_B():
    turtle.sety(turtle.window_height() // 2.5)
    return turtle.ycor()

def row_C():
    turtle.sety(-turtle.window_height() // 2.5)
    return turtle.ycor()


def row_D():
    turtle.sety(-turtle.window_height() // 1.5)
    return turtle.ycor()

def col_1():
    turtle.setx(-turtle.window_width() // 1.5)
    return turtle.xcor()

def col_2():
    turtle.setx(-turtle.window_width() // 2.5)
    return turtle.xcor()

def col_3():
    turtle.setx(turtle.window_width() // 2.5)
    return turtle.xcor()

def col_4():
    turtle.setx(turtle.window_width() // 1.5)
    return turtle.xcor()
'''

A = turtle.sety(turtle.window_height() // 1.5)

'''
B = row_B()
C = row_C()
D = row_D()
'''


one = turtle.setx(-turtle.window_width() // 1.5)

'''
two = col_2()
three = col_3()
four = col_4()
'''


'''
turtle.goto(0,0)
rows_col = [[A,B,C,D], [one,two,three,four]]
'''




'''
for row in rows_col[0]:
    for col in rows_col[1]:
        user_input = input('What is your move?')
        if user_input in rows_col:
            turtle.goto(user_input)

'''


# row_input = turtle.textinput('','What row do you want to move?')
A
print(turtle.ycor())


# col_input = turtle.textinput('', 'What col do you want to move?')
one
print(turtle.xcor())



print(turtle.xcor(),turtle.ycor())





def turtle_input():
    move_input = turtle.textinput('','Make a move')
    make_move = turtle.write(move_input, move= False, align = 'left', font = ('Arial', 65,'normal'))
    return make_move


turtle.pd()
turtle_input()
print(turtle.xcor(),turtle.ycor())









turtle.done()