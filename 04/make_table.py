import turtle

width=6;
height=6;

while width>0:
    turtle.penup()
    turtle.goto(width*100,0)
    turtle.pendown()
    turtle.goto(width*100,500)
    width-=1

while height>0:
    turtle.penup()
    turtle.goto(100,(height-1)*100)
    turtle.pendown()
    turtle.goto(600, (height-1)*100)
    height-=1

    
turtle.exitonclick()

