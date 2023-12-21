from turtle import Turtle, Screen, forward, backward, left, right, clear, home, penup
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_strart = -50
x_stat = -230
final = 230
game_on = False
turtles = []

for turtle_index in range(0, 6):
    turtle_color = (colors[turtle_index])
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x=x_stat, y=y_strart)
    y_strart += 30
    turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turle in turtles:
        random_move = random.randint(0, 10)
        turle.forward(random_move)
        x_position = turle.xcor()

        if x_position >= final:

            wining_color = turle.pencolor()
            if wining_color == user_bet:
                print(f"You win! Wining color is {wining_color}")
            else:
                print(f"You lost! Wining color is {wining_color}")

            game_on = False


screen.exitonclick()
