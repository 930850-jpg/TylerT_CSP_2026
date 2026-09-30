#119 Python File
import turtle as trtl
import random 
wn = trtl.Screen()
wn.tracer(0)
painter = trtl.Turtle()
painter.speed(0)

#Set up painting 
starting_x = -125
end_x = 125
starting_y = -200
end_y = 200
painting_orient = trtl.textinput("MAKING A PAINTING", "Portrait(P) or Landscape(L)?").lower()
if (painting_orient == "l"):
  starting_x = -200
  end_x = 200
  starting_y = -125
  end_y = 125
painter.penup()
painter.goto(starting_x, starting_y)
painter.pendown()
painter.goto(end_x, starting_y)
painter.goto(end_x, end_y)
painter.goto(starting_x, end_y)
painter.goto(starting_x, starting_y)

#Draw Frame Design
wn.tracer(1)
frame_design = trtl.textinput("MAKING A PAINTING","Frame design, Wavy(W) or ZigZag(Z)?").lower()
if (frame_design == "w"):
  painter.penup()
  painter.right(90)
  painter.forward(10)
  painter.pendown()
  painter.left(45)
  while painter.xcor() < end_x:
    painter.circle(20, 90)
    if painter.xcor() > end_x:
      break
    painter.circle(-20, 90) 
  painter.forward(7)
  painter.penup()
  painter.goto(end_x, starting_y)
  painter.setheading(0)
  painter.forward(10)
  painter.pendown()
  painter.left(45)
  while painter.ycor() < end_y:
    painter.circle(15, 90)
    if painter.ycor() > end_y:
      break
    painter.circle(-15, 90)
  painter.penup()
  painter.goto(starting_x, end_y)
  painter.setheading(0)
  painter.left(90)
  painter.forward(10)
  painter.pendown()
  painter.right(45)
  while painter.xcor() < end_x:
    painter.circle(-20, 90)
    if painter.xcor() > end_x:
      break
    painter.circle(20, 90)  
  painter.forward(7)
  painter.penup()
  painter.goto(starting_x, starting_y)
  painter.setheading(0)
  painter.backward(10)
  painter.pendown()
  painter.left(135)
  while painter.ycor() < end_y:
    painter.circle(-15, 90)
    if painter.ycor() > end_y:
      break
    painter.circle(15, 90)
  painter.forward(7)
















wn.mainloop()