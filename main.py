import turtle as t
import random

tam = t.Turtle()  # Red
tem = t.Turtle()  # Green
tim = t.Turtle()  # Blue
screen = t.Screen()

colors = ["red", "green", "blue"]
turtle_list = [tam, tem, tim]

message_turtle = t.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(-230, -140)

screen.setup(width=500, height=400)

player_1_name = screen.textinput(title="What is your name?",
                                prompt="What is your name, player 1?")
player_2_name = screen.textinput(title="What is your name?",
                                prompt="What is your name, player 2?")
player_1_bet = screen.textinput(title=f"{player_1_name} - Place your bet",
                                prompt="Which turtle will win the race? Enter a color: (red, green, blue)")
player_2_bet = screen.textinput(title=f"{player_2_name} - Place your bet",
                                prompt="Which turtle will win the race? Enter a color: (red, green, blue)")
chore = screen.textinput(title="Enter a chore", prompt="What chore will the loser(s) have to do?")


def draw_finish_line():
    finish_line = t.Turtle()
    finish_line.hideturtle()
    finish_line.pensize(10)
    finish_line.color("yellow")
    finish_line.penup()
    finish_line.goto(200, 110)
    finish_line.pendown()
    finish_line.right(90)
    finish_line.forward(220)


def start_of_race():
    start_y = 60
    space_between = 60
    for turtle, color in zip(turtle_list, colors):
        turtle.color(color)
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(x=-230, y=start_y)
        start_y -= space_between


def race_turtles():
    while True:
        for turtle in turtle_list:
            distance = random.randint(0, 5)
            turtle.forward(distance)
            if turtle.xcor() >= 200:  # Adjusted finish line
                return turtle.color()[0]


def display_result(winner, player_1_bet, player_2_bet, chore):
    if winner == player_1_bet and winner != player_2_bet:
        message = f"{player_1_name} wins! 😂 {player_1_name} has to {chore}..."
    elif winner == player_2_bet and winner != player_1_bet:
        message = f"{player_2_name} wins! 😂 {player_2_name} has to {chore}..."
    elif winner != player_1_bet and winner != player_2_bet:
        message = f"You both lose. 😖 You both have to {chore}..."
    else:
        message = "It's a draw. No one has to do the chore."
    message_turtle.write(message, move=False, align="left", font=("Arial", 12, "normal"))


draw_finish_line()
start_of_race()
winner = race_turtles()
display_result(winner, player_1_bet, player_2_bet, chore)

screen.exitonclick()
