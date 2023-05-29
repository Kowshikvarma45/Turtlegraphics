from turtle import Turtle, Screen
import random
color = ["violet", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
my_Screen = Screen()
my_Screen.setup(width=500, height=400)
is_on = False
x = -240
y = -60
def turtle_go_to(x, y, turtle_name):
    turtle_name.penup()
    turtle_name.goto(x, y)

for i in range(0,6):
    new_turtle = Turtle()
    turtle_color = color[i]
    new_turtle.color(turtle_color)
    new_turtle.shape("turtle")
    all_turtles.append(new_turtle)
    turtle_go_to(x, y, new_turtle)
    y += 30

user_guess = my_Screen.textinput(title="Make your bet!!", prompt="which coloured turtle win the race? : ")

if user_guess:
    is_on = True
while is_on:
    for turtles in all_turtles:
      if turtles.xcor() > 240:
          is_on = False
          winner = turtles.pencolor()
          if winner == user_guess:
              print(f"you won the game, the winning turtle is {winner}")
              break
          else:
              print(f"you lost it!,the winning turtle is {winner}")
              break


      distance = random.randint(1, 10)
      turtles.fd(distance)


my_Screen.exitonclick()
