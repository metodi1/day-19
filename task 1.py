from turtle import Turtle, Screen, forward, backward, left, right, clear, home, penup

tim = Turtle()
screen = Screen()


def move_forward():
    forward(10)


def move_back():
    backward(10)


def move_left():
    left(10)


def move_right():
    right(10)


def clear_path():
    clear()
    penup()
    home()


screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_path, "c")

screen.listen()

screen.exitonclick()
