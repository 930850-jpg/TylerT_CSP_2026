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
painter.penup() #make the center of the painting
painter.goto(starting_x, starting_y)
painter.pendown()
painter.goto(end_x, starting_y)
painter.goto(end_x, end_y)
painter.goto(starting_x, end_y)
painter.goto(starting_x, starting_y)

#Draw Frame Design
wn.tracer(1)
frame_design = trtl.textinput("MAKING A PAINTING","Frame design, Wavy(W) or ZigZag(Z)?").lower()
painter.fillcolor("gold")
last_x = 0
last_y = 0
last_x2 = 0
last_y2 = 0 #variables used to connect corners of the frame
if (frame_design == "w"): #Wavy design
  painter.begin_fill()
  painter.penup()
  painter.right(90)
  painter.forward(10)
  painter.pendown()
  painter.left(45)
  last_x2 = painter.xcor()
  last_y2 = painter.ycor()
  if painting_orient == "l":
    while painter.xcor() < end_x:
      painter.circle(15, 90)
      if painter.xcor() > end_x:
        break
      painter.circle(-15, 90) 
  else:
    while painter.xcor() < end_x:
      painter.circle(20, 90)
      if painter.xcor() > end_x:
        break
      painter.circle(-20, 90) 
  last_x = painter.xcor()
  last_y = painter.ycor()
  painter.goto(end_x+10,starting_y)
  painter.end_fill()
  painter.goto(last_x,last_y)
  painter.begin_fill()
  for i in range(2):
    painter.penup()
    painter.goto(starting_x, starting_y)
    painter.setheading(0)
    painter.backward(10)
    painter.pendown()
    if i == 1:
      break
    painter.goto(last_x2,last_y2)
  painter.left(135)
  if painting_orient == "l":
    while painter.ycor() < end_y:
      painter.circle(-20, 90)
      if painter.ycor() > end_y:
        break
      painter.circle(20, 90) 
  else:
    while painter.ycor() < end_y:
      painter.circle(-15, 90)
      if painter.ycor() > end_y:
        break
      painter.circle(15, 90)
  painter.end_fill()
  last_x2 = painter.xcor()
  last_y2 = painter.ycor()
  painter.begin_fill()
  for i in range(2):
    painter.penup()
    painter.goto(end_x, starting_y)
    painter.setheading(0)
    painter.forward(10)
    painter.pendown()
    if i == 1:
      break
    painter.goto(last_x,last_y)
  painter.left(45)
  if painting_orient == "l":
    while painter.ycor() < end_y:
      painter.circle(20, 90)
      if painter.ycor() > end_y:
        break
      painter.circle(-20, 90)     
  else:
    while painter.ycor() < end_y:
      painter.circle(15, 90)
      if painter.ycor() > end_y:
        break
      painter.circle(-15, 90)
  painter.end_fill()
  last_x = painter.xcor()
  last_y = painter.ycor()
  painter.begin_fill()
  for i in range(2):
    painter.penup()
    painter.goto(starting_x, end_y)
    painter.setheading(0)
    painter.left(90)
    painter.forward(10)
    painter.pendown()
    if i == 1:
      break
    painter.goto(last_x2,last_y2)
  painter.right(45)
  if painting_orient == "l":
    while painter.xcor() < end_x:
      painter.circle(-15, 90)
      if painter.xcor() > end_x:
        break
      painter.circle(15, 90)
  else:
    while painter.xcor() < end_x:
      painter.circle(-20, 90)
      if painter.xcor() > end_x:
        break
      painter.circle(20, 90)  
  painter.goto(last_x,last_y)
  painter.end_fill()
else: #Zigzag pattern
  painter.begin_fill()
  painter.penup()
  painter.goto(starting_x,starting_y-5)
  painter.pendown()
  last_x = painter.xcor()
  last_y = painter.ycor()
  while painter.xcor() < end_x:
    painter.goto(painter.xcor()+25, starting_y-15)
    if painter.xcor() > end_x:
      break
    painter.goto(painter.xcor()+25, starting_y-5)
  painter.goto(end_x+5,starting_y)
  painter.end_fill()
  painter.begin_fill()
  painter.left(90)
  while painter.ycor() < end_y:
    painter.goto(end_x+15, painter.ycor()+25)
    if painter.ycor() > end_y:
      break
    painter.goto(end_x+5, painter.ycor()+25)
  painter.end_fill()
  last_x2 = painter.xcor()
  last_y2 = painter.ycor()
  painter.begin_fill()
  for i in range(2):
    painter.penup()
    painter.goto(starting_x-5,starting_y)
    painter.pendown()
    if i ==1:
      break
    painter.goto(last_x,last_y)
  while painter.ycor() < end_y:
    painter.goto(starting_x-15, painter.ycor()+25)
    if painter.ycor() > end_y:
      break
    painter.goto(starting_x-5, painter.ycor()+25)
  painter.goto(starting_x,end_y+5)
  painter.end_fill()
  painter.begin_fill()
  while painter.xcor() < end_x:
    painter.goto(painter.xcor()+25, end_y+15)
    if painter.xcor() > end_x:
      break
    painter.goto(painter.xcor()+25, end_y+5)
  painter.goto(last_x2,last_y2)
  painter.end_fill()
  #color in the rest that was missed
  painter.pencolor("gold")
  painter.begin_fill()
  for i in range(2):
    painter.goto(starting_x-5,starting_y)
    if i == 1:
      break
    painter.goto(end_x+5,starting_y)
    painter.goto(last_x2,last_y2)
  painter.end_fill()


#Remake the center of the painting (code breaks if the earlier one doesn't run I have no idea why but if it works dont change it)

painter.setheading(0)
painter.pencolor("black")
painter.fillcolor("white")
painter.begin_fill()
painter.penup()
painter.goto(starting_x, starting_y)
painter.pendown()
painter.goto(end_x, starting_y)
painter.goto(end_x, end_y)
painter.goto(starting_x, end_y)
painter.goto(starting_x, starting_y)
painter.end_fill()












wn.mainloop()