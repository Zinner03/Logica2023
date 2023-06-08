import turtle

wn = turtle.Screen()
wn.title("Pong by: Esteban Garcia")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
# Raqueta A
raqueta_a = turtle.Turtle()
raqueta_a.speed(0)
raqueta_a.shape("square")
raqueta_a.color("white")
raqueta_a.shapesize(stretch_wid=5, stretch_len=1)
raqueta_a.penup()
raqueta_a.goto(-350, 0)

# Raqueta B
raqueta_b = turtle.Turtle()
raqueta_b.speed(0)
raqueta_b.shape("square")
raqueta_b.color("white")
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup()
raqueta_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("red")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.7
pelota.dy = -0.7

# Estilo
estilo = turtle.Turtle()
estilo.speed(0)
estilo.color("white")
estilo.penup()
estilo.hideturtle()
estilo.goto(0, 260)
estilo.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 21, "normal"))


# Funcion teclado
def raqueta_a_arriba():
    y = raqueta_a.ycor()
    y += 20
    raqueta_a.sety(y)

def raqueta_a_abajo():
    y = raqueta_a.ycor()
    y -= 20
    raqueta_a.sety(y)

def raqueta_b_arriba():
    y = raqueta_b.ycor()
    y += 20
    raqueta_b.sety(y)

def raqueta_b_abajo():
    y = raqueta_b.ycor()
    y -= 20
    raqueta_b.sety(y)

# Teclas

wn.listen()
wn.onkeypress(raqueta_a_arriba, "w")
wn.onkeypress(raqueta_a_abajo, "s")
wn.onkeypress(raqueta_b_arriba, "Up")
wn.onkeypress(raqueta_b_abajo, "Down")

# Ciclo principal
while True:
    wn.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Deteccion del borde
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy += -1


    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1


    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_a += 1
        estilo.clear()
        estilo.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 21, "normal"))



    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_b += 1
        estilo.clear()
        estilo.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 21, "normal"))


    # Colisiones entre raquetas y pelota
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < raqueta_b.ycor() + 40 and pelota.ycor() > raqueta_b.ycor() -40):
        pelota.setx(340)
        pelota.dx *= -1
        
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < raqueta_a.ycor() + 40 and pelota.ycor() > raqueta_a.ycor() -40):
        pelota.setx(-340)
        pelota.dx *= -1     
