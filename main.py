import turtle

#intro
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('lightblue')
t = turtle.Turtle()
t2 = turtle.Turtle()
t.hideturtle()
t.write("Turtle Presentation", font=("arial", 24, "bold"), align="center")

t2.penup()
turtle.addshape("sun.gif")
t2.shape("sun.gif")
t2.goto(150,-150)
a=t2.stamp()

turtle.addshape("beach.gif")
t2.shape("beach.gif")
t2.goto(-150,150)
b=t2.stamp()

#circle
t.penup()
t.goto(0,-50)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.circle(25)
t.end_fill()


#favfoods
enter = input("Press Enter for the Next Slide")
t.clear()
t2.clear()
t2.hideturtle()


screen.bgcolor('light pink')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Foods", font=("arial", 24, "bold"), align="center")
t.penup()


t.goto(-200, 50)
t.write("Mac and Cheese", font=("arial", 18, "bold"), align="center" )
t.penup()


t.goto(0, 50)
t.write("Pasta", font=("arial", 18, "bold"), align="center" )
t.penup()


t.goto(200, 50)
t.write("Pizza", font=("arial", 18, "bold"), align="center" )

turtle.addshape("macandcheese.gif")
t2.shape("macandcheese.gif")
t2.goto(-200,-50)
c=t2.stamp()

turtle.addshape("pizza.gif")
t2.shape("pizza.gif")
t2.goto(200,-50)
d=t2.stamp()


#triangle
t.penup()
t.goto(-50,-50)
t.pendown()
t.fillcolor('deep pink')
t.begin_fill()
t.goto(50,-50)
t.goto(0,0)
t.goto(-50,-50)
t.end_fill()



#hobbies
enter  = input("Press Enter for the Next Slide")
t.clear()
t2.clearstamps()

screen.bgcolor('pale green')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Hobbies", font=("arial", 24, "bold"), align="center")
t.penup()

t.goto(-200, 100)
t.write("Running", font=("arial", 18, "bold") , align="center")

t.goto(200, 100)
t.write("Shopping", font=("arial", 18, "bold") , align="center")

t.goto(-200, -200)
t.write("Playing Lacrosse", font=("arial", 18, "bold"), align="center" )

t.goto(200, -200)
t.write("Hanging Out", font=("arial", 18, "bold"), align="center" )

t.goto(200, -230)
t.write("With Friends", font=("arial", 18, "bold"), align="center" )

turtle.addshape("running.gif")
t2.shape("running.gif")
t2.goto(-200,0)
f=t2.stamp()

turtle.addshape("friends.gif")
t2.shape("friends.gif")
t2.goto(200,-100)
g=t2.stamp()

#square
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor('medium seagreen')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


#favmovie
enter  = input("Press Enter for the Next Slide")
t.clear()
t2.clearstamps()

screen.bgcolor('slate blue')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Movie", font=("arial", 24, "bold"), align="center")
t.penup()

t.goto(0,90)
t.write("Tangled", font=("arial", 18, "bold"), align="center" )

turtle.addshape("tangled.gif")
t2.shape("tangled.gif")
t2.goto(-100,20)
h=t2.stamp()

turtle.addshape("flower.gif")
t2.shape("flower.gif")
t2.goto(100,20)
j=t2.stamp()

#rectangle
t.penup()
t.goto(-50,-150)
t.pendown()
t.fillcolor('dark violet')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()

#favsport
enter  = input("Press Enter for the Next Slide")
t.clear()
t2.clearstamps()

screen.bgcolor('pale goldenrod')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Sport", font=("arial", 24, "bold"), align="center")
t.penup()

t.goto(0,100)
t.write("Lacrosse", font=("arial", 18, "bold"), align="center" )

turtle.addshape("lax.gif")
t2.shape("lax.gif")
t2.goto(-100,50)
k=t2.stamp()

turtle.addshape("lacrosse.gif")
t2.shape("lacrosse.gif")
t2.goto(100,50)
l=t2.stamp()

#haflcircle
t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor('tomato')
t.begin_fill()
t.circle(30,180)
t.end_fill()



turtle.done()