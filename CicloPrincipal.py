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
