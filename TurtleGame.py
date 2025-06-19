import turtle
import random

# Oyun ekranını oluşturma
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Catch the Turtle")
turtle_screen.setup(700, 600)
turtle_screen.tracer(0)

# Kaplumbağayı oluşturma
tostos = turtle.Turtle()
tostos.shape("turtle")
tostos.color("purple")
tostos.speed(10)
tostos.penup()
tostos.hideturtle()

# Skor ve zaman göstergesi
score = 0
time_left = 30

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.write(f"Score: {score}", font=("Arial", 15, "bold"))

time_writer = turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(150, (250))
time_writer.write(f"Time: {time_left}", font=("Arial", 15, "bold"))

# Kaplumbağayı rastgele konuma taşı
def move_tostos():
    if time_left > 0:
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        tostos.goto(x, y)
        tostos.showturtle()
        turtle_screen.update()
        turtle_screen.ontimer(move_tostos, 800)

# Kaplumbağaya tıklanırsa puan alma
def click(x, y):
    global score
    if tostos.distance(x, y) < 30:
        score += 1
        score_writer.clear()
        score_writer.write(f"Score: {score}", font=("Arial", 15, "bold"))

# Zamanlayıcı
def count_down():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_writer.clear()
        time_writer.write(f"Time: {time_left}", font=("Arial", 15, "bold"))
        turtle_screen.ontimer(count_down, 1000)
    else:
        tostos.hideturtle()
        turtle_screen.update()
        score_writer.goto(0, 0)
        score_writer.write(f"Oyun Bitti Teşekkürler Oynadığınız İçin Final Score: {score}", align="center", font=("Arial", 15, "bold"))

# Başlatma
tostos.onclick(click)
move_tostos()
count_down()

turtle_screen.mainloop()
