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
