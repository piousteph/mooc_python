"""
Projet Vasarely
par Stephane Tinseau
"""
import turtle

COLOR = ("blue", "black", "red")

def hexagone(x, y, l):
    """ Desine un hexagone a la position x,y de longueur l """
    
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for i in range(3):  # à chaque itération, trace un losange
        angle = 120
        turtle.fillcolor(COLOR[i])
        turtle.begin_fill()
        for j in range(4): # à chaque itération, trace un segment
            turtle.forward(l)
            turtle.left(angle)
            angle = 180 - angle
        turtle.end_fill()
        turtle.right(120)
        turtle.hideturtle()

def pavage(cx, cy, l):
    """ Creer un pavage de cx hexagones sur cy hexagone de longueur l """

    i = 0
    for y in range(-(l*cx)-5, (l*cy)-5, l):
        for x in range(-(l*(cx-i%2)), (l*(cy-i%2)), l*3):
            hexagone(x, y, l)
        i += 1

#turtle.tracer(0, 0)
pavage(3, 3, 30)
#turtle.update()
turtle.done()