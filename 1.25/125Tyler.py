#---------Imports-----------#
import turtle as trtl
import random as rand
from functools import partial
import keyboard as kb
wn = trtl.Screen()
wn.tracer(0)
#---------------------------#

#--------------Custom shapes and images-----------------#
explosion = ((0, 10), (5, 8), (10, 10), (8, 5), 
    (10, 0), (8, -5), (10, -10), (5, -8), (0,-10), (-5,-8), (-10,-10), (-8,-5),(-10,0), (-8,5), (-10, 10), (-5,8))
wn.register_shape("explosion", explosion)
#-------------------------------------------------------#

#------Initialize Variables---------#
ammo = 10
loaded_ammo = 2
max_ammo_loaded = 2
damage = 1
size_list = ["small", "small", "small", "small", "small"]
small_enemy_health = 1
big_enemy_health = 5
health = 100
wave = 0
enemy_list = []
#-----------------------------------#

#-----Initialize Turtles for writing and sprites-----#
ammo_counter = trtl.Turtle()
ammo_counter.hideturtle()
ammo_counter.penup()
ammo_counter.goto(180,-225)
health_counter = trtl.Turtle()
health_counter.hideturtle()
health_counter.penup()
health_counter.goto(0,-225)
reloader = trtl.Turtle()
reloader.hideturtle()
reloader.penup()
reloader.goto(-180,-225)
wave_counter = trtl.Turtle()
shot_color_list = ["yellow" ,"maroon", "orange"]
shot_sprite_list = []
for s in shot_color_list:
  shot_sprite = trtl.Turtle(shape="explosion")
  color = shot_color_list.pop()
  shot_sprite.speed(0)
  shot_sprite.penup()
  shot_sprite.fillcolor(color)
  shot_sprite_list.append(shot_sprite)
  shot_sprite.hideturtle()
#----------------------------------------------------#

#--------------------Functions------------------------------#
def update_counters():
  ammo_counter.clear()
  reloader.clear()
  health_counter.clear()
  ammo_counter.write("Ammo:" + str(ammo), align='center', font=("Arial", 20, "normal"))
  reloader.write(str(loaded_ammo) + "/" + str(max_ammo_loaded), align='center', font=("Arial", 20, "normal"))
  health_counter.write("Health:" + str(health), align='center', font=("Arial", 20, "normal"))

def new_enemies():
  global enemy, enemy_list
  for e in size_list:
    enemy = trtl.Turtle(shape="circle")
    enemy.speed(0)
    enemy.penup()
    enemy.onclick(partial(enemy_shot, enemy))
    enemy_list.append(enemy)
    if e == "big":
      enemy.shapesize(3)

def move_enemies():
  for enemy in enemy_list:
    enemy.goto(rand.randint(-225,225),rand.randint(-200,225))

def enemy_shot(enemy, x, y):
  global ammo, loaded_ammo
  clicked_enemy = enemy
  if ammo != 0:
    if loaded_ammo != 0:
      loaded_ammo -= 1
      update_counters()
      if clicked_enemy in enemy_list:
        enemy_list.remove(clicked_enemy)
        clicked_enemy.hideturtle()
      move_enemies()
      
def shot_vfx(x,y):
  for shot_sprite in shot_sprite_list:
    shot_sprite.goto(x+rand.randint(-10,10),y+rand.randint(-10,10))
    shot_sprite.showturtle()
  for shot_sprite in shot_sprite_list:
    shot_sprite.hideturtle()

def reload():
  global ammo, loaded_ammo, max_ammo_loaded
  while loaded_ammo != max_ammo_loaded:
    loaded_ammo += 1
    ammo -= 1
  update_counters()

#----------------------------------------------------------#

#------------------Events----------------#
wn.tracer(1)
new_enemies()
move_enemies()

wn.listen()
wn.onclick(shot_vfx)
wn.onkeypress(reload, "r")




wn.setup(width=500, height=500)
wn.cv._rootwindow.resizable(False, False)
wn.mainloop()