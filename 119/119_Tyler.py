#119 Python File
import turtle as trtl
import random 
wn = trtl.Screen()
wn.tracer(0)
painter = trtl.Turtle()
painter.speed(0)
paintbrush = ((-1, 7), (1, 7), (1, -3), (3, -6), 
                  (2, -7), (1, -6), (0, -7), (-1, -6), (-2,-7), (-3,-6), (-1,-3), (-1,7))
wn.register_shape("paintbrush", paintbrush)
painter.shape("paintbrush")
color_list = ["black", "gray", "silver", "rosybrown", "firebrick", #List of every python color
    "red", "darksalmon", "sienna", "sandybrown", "bisque", "tan",
    "moccasin", "gold", "darkkhaki",
    "olivedrab", "chartreuse", "palegreen", "darkgreen", "seagreen",
    "mediumspringgreen", "paleturquoise", "darkcyan",
    "darkturquoise", "deepskyblue", "slategray", "royalblue",
    "navy", "blue", "mediumpurple", "darkorchid", "plum", 
    "mediumvioletred", "palevioletred",

    "grey", "lightgray", "lightcoral", "maroon", "mistyrose",
    "coral", "seashell", "peachpuff", "darkorange", "navajowhite",
    "orange", "darkgoldenrod", "lemonchiffon", "olive",
    "yellowgreen", "lawngreen", "lightgreen", "mediumseagreen",
    "mediumaquamarine", "mediumturquoise", "darkslategray",
    "cadetblue", "skyblue", "dodgerblue", "slategray",
    "darkblue", "slateblue", "darkviolet", "violet",
    "fuchsia", "deeppink", "crimson",

    "dimgray", "darkgray", "lightgrey", "indianred", "darkred",
    "salmon", "orangered", "chocolate", "peru", "burlywood",
    "blanchedalmond", "wheat", "goldenrod", "khaki",
    "darkolivegreen", "forestgreen", "green", "springgreen",
    "aquamarine", "darkslategray", "aqua", "powderblue",
    "lightskyblue", "lightslategray", "lightsteelblue", "lavender",
    "mediumblue", "darkslateblue", "blueviolet", "mediumpurple",
    "purple", "magenta", "hotpink", "pink",

    "dimgrey", "darkgrey", "gainsboro", "brown", "tomato",
    "lightsalmon", "saddlebrown", "papayawhip",
    "cornsilk", "palegoldenrod", "lightyellow", "yellow",
    "greenyellow", "darkseagreen", "limegreen", "lime",
    "turquoise", "lightcyan", "teal", "cyan", "lightblue", "steelblue",
    "lightslategray", "cornflowerblue", "midnightblue",
    "mediumslateblue", "indigo", "thistle", "darkmagenta", "orchid",
    "lightpink"]

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
canvas_color = trtl.textinput("MAKING A PAINTING","What color should the background of the canvas be?").lower()
painter.setheading(0)
painter.pencolor("black")
painter.fillcolor("white")
if canvas_color in color_list:
  painter.fillcolor(canvas_color)
painter.begin_fill()
painter.penup()
painter.goto(starting_x, starting_y)
painter.pendown()
painter.goto(end_x, starting_y)
painter.goto(end_x, end_y)
painter.goto(starting_x, end_y)
painter.goto(starting_x, starting_y)
painter.end_fill()

#Draw shapes in the canvas as "abstract" art
wn.tracer(1)
for shapes in range(200):
  painter.setheading(0)
  painter.penup()
  painter.pencolor(random.choice(color_list))
  painter.fillcolor(random.choice(color_list))
  painter.goto(random.randint(starting_x+15,end_x-15),random.randint(starting_y+7,end_y-35))
  painter.pendown()
  painter.begin_fill()
  painter.circle(random.randint(5,20),360,random.randint(3,15))
  painter.end_fill()


painter.penup()
painter.goto(250, 0)
painter.setheading(90)






wn.mainloop()