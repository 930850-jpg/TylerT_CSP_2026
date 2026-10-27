#---------Imports-----------#
import turtle as trtl
import random as rand
from functools import partial
import time
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
reload_delay = 1
damage = 1
health = 100
#----#
size_list = ["small", "small", "small", "small", "small"]
small_enemy_health = 1
big_enemy_health = 5
small_enemy_list = []
big_enemy_list = []
#----#
wave = 0
small_defeated = 0
big_defeated = 0
#-----------------------------------#

#-----Initialize Turtles for writing and sprites-----#
ammo_counter = trtl.Turtle()
ammo_counter.hideturtle()
ammo_counter.penup()
ammo_counter.goto(160,-225)
health_counter = trtl.Turtle()
health_counter.hideturtle()
health_counter.penup()
health_counter.goto(-160,-225)
reloader = trtl.Turtle()
reloader.hideturtle()
reloader.penup()
reloader.goto(160,-200)
wave_counter = trtl.Turtle()
wave_counter.hideturtle()
wave_counter.penup()
wave_counter.goto(-5,200)
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
  wave_counter.clear()
  ammo_counter.write("Ammo: " + str(ammo), align='center', font=("Arial", 20, "normal"))
  reloader.write(str(loaded_ammo) + "/" + str(max_ammo_loaded), align='center', font=("Arial", 20, "normal"))
  health_counter.write("Health: " + str(health), align='center', font=("Arial", 20, "normal"))
  wave_counter.write("Wave: " + str(wave), align='center', font=("Arial", 20, "normal"))

def new_enemies():
  global enemy, big_enemy, small_enemy_list, big_enemy_list
  for e in size_list:
    if e =="small":
      enemy = trtl.Turtle(shape="circle")
      enemy.speed(0)
      enemy.penup()
      enemy.onclick(partial(small_enemy_shot, enemy))
      small_enemy_list.append(enemy)
    if e == "big":
      big_enemy = trtl.Turtle(shape="circle")
      big_enemy.shapesize(3)
      big_enemy.speed(0)
      big_enemy.penup()
      big_enemy.onclick(partial(big_enemy_shot, big_enemy))
      big_enemy_list.append(big_enemy)

def move_enemies():
  global enemy, big_enemy
  for enemy in small_enemy_list:
    enemy.goto(rand.randint(-100,150),rand.randint(-100,150))
    if (abs(enemy.xcor() - enemy.xcor()) < 30) and (abs(enemy.ycor() - enemy.ycor()) < 30):
      enemy.goto(enemy.xcor() + 50, enemy.ycor() + 50)
  if big_enemy_list != []:
    for big_enemy in big_enemy_list:
      big_enemy.goto(rand.randint(-100,150),rand.randint(-100,150))
      if (abs(enemy.xcor() - big_enemy.xcor()) < 30) and (abs(enemy.ycor() - big_enemy.ycor()) < 30):
        enemy.goto(enemy.xcor() + 50, enemy.ycor() + 50)
    
def small_enemy_shot(enemy, x, y):
  global ammo, loaded_ammo, small_defeated, big_defeated
  clicked_enemy = enemy
  if ammo != 0:
    if loaded_ammo != 0:
      loaded_ammo -= 1
      update_counters()
      if clicked_enemy in small_enemy_list:
        small_enemy_list.remove(clicked_enemy)
        clicked_enemy.hideturtle()
      move_enemies()
    if small_enemy_list == []:
      small_defeated = 1
    if big_defeated == 1 and small_defeated == 1:
      end_wave()
    elif small_defeated == 1 and big_enemy_list == []:
      end_wave()
    
def big_enemy_shot(big_enemy, x, y):
  global ammo, loaded_ammo, big_enemy_health, big_defeated, small_defeated
  clicked_enemy = big_enemy
  if ammo != 0:
    if loaded_ammo != 0:
      loaded_ammo -= 1
      big_enemy_health -= damage
      update_counters()
      if clicked_enemy in big_enemy_list:
        if big_enemy_health <= 0:
          big_enemy_list.remove(clicked_enemy)
          clicked_enemy.hideturtle()
      move_enemies()
    if big_enemy_list == []:
      big_defeated = 1
    if big_defeated == 1 and small_defeated == 1:
      end_wave()

def shot_vfx(x,y):
  for shot_sprite in shot_sprite_list:
    shot_sprite.goto(x+rand.randint(-10,10),y+rand.randint(-10,10))
    shot_sprite.showturtle()
  for shot_sprite in shot_sprite_list:
    shot_sprite.hideturtle()

def reload():
  global ammo, loaded_ammo, max_ammo_loaded
  while loaded_ammo != max_ammo_loaded:
    time.sleep(reload_delay)
    loaded_ammo += 1
    ammo -= 1
    update_counters()

def new_wave():
  update_counters()
  new_enemies()
  move_enemies()

def end_wave():
  global ammo, loaded_ammo, max_ammo_loaded
  ammo += 5
  loaded_ammo = max_ammo_loaded
  wave_counter.clear()
  wave_counter.write("WAVE: " + str(wave) + " DEFEATED", align='center', font=("Arial", 20, "normal"))
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