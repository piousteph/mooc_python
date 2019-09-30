import turtle
for i in range(3):  # à chaque itération, trace un losange
   angle = 120
   for j in range(4): # à chaque itération, trace un segment
       turtle.forward(100)
       turtle.left(angle)
       angle = 180 - angle
   turtle.right(120)
turtle.hideturtle()
turtle.done()