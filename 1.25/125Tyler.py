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
initial_small_enemy_health = 1
small_enemy_health = 1
big_enemy_health = 5
initial_big_enemy_health = 5
small_enemy_list = []
big_enemy_list = []
#----#
wave = 0
wave_timer = 15000
small_defeated = 0
big_defeated = 0
ammo_after_wave = 5
#----#
upgrade_list = ["+1 to weapon damage", "+1 ammo to barrel", "+25 health", "+5 extra ammo every wave","wave timer increase by 5"]
late_upgrade_list = ["lower enemy health by 2", "faster reload by 0.5", "remove a small enemy"]
debuff_list = ["add small enemy", "small enemy turns into big enemy", "2x small enemy health", "2x big enemy health"]
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
upgrade_writer = trtl.Turtle()
upgrade_writer.hideturtle()
upgrade_writer.penup()
upgrade_writer.goto(0,150)
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
      enemy.shapesize(1.5)
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
    enemy.goto(rand.randint(-150,150),rand.randint(-100,150))
    if (abs(enemy.xcor() - enemy.xcor()) < 40) and (abs(enemy.ycor() - enemy.ycor()) < 40):
      enemy.goto(enemy.xcor() - 50, enemy.ycor() + 50)
  if big_enemy_list != []:
    for big_enemy in big_enemy_list:
      big_enemy.goto(rand.randint(-150,150),rand.randint(-100,150))
      if (abs(enemy.xcor() - big_enemy.xcor()) < 40) and (abs(enemy.ycor() - big_enemy.ycor()) < 40):
        enemy.goto(enemy.xcor() - 50, enemy.ycor() + 50)
    
def small_enemy_shot(enemy, x, y):
  global ammo, loaded_ammo, small_defeated, big_defeated, small_enemy_health
  clicked_enemy = enemy
  if ammo != 0:
    if loaded_ammo != 0:
      loaded_ammo -= 1
      small_enemy_health -= damage
      update_counters()
      if clicked_enemy in small_enemy_list:
        if small_enemy_health <=0:
          small_enemy_health = initial_small_enemy_health
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
  global ammo, loaded_ammo, big_enemy_health, big_defeated, small_defeated, damage
  clicked_enemy = big_enemy
  if ammo != 0:
    if loaded_ammo != 0:
      loaded_ammo -= 1
      big_enemy_health -= damage
      update_counters()
      if clicked_enemy in big_enemy_list:
        if big_enemy_health <= 0:
          big_enemy_health = initial_big_enemy_health
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
  global wave
  wave += 1
  wn.listen()
  update_counters()
  new_enemies()
  move_enemies()

def end_wave():
  global ammo, loaded_ammo, max_ammo_loaded, small_defeated, big_defeated
  small_defeated = 0
  big_defeated = 0
  ammo += ammo_after_wave
  loaded_ammo = max_ammo_loaded
  wave_counter.clear()
  wave_counter.write("WAVE: " + str(wave) + " DEFEATED", align='center', font=("Arial", 20, "normal"))
  upgrades()
  if wave % 2 == 0:
    debuffs()
  new_wave()

def upgrades():
  global ammo_after_wave, damage, health, max_ammo_loaded, wave_timer
  upgrade_pick1 = rand.choice(upgrade_list)
  upgrade_list.remove(upgrade_pick1)
  upgrade_pick2 = rand.choice(upgrade_list)
  upgrade_list.remove(upgrade_pick2)
  upgrade_pick3 = rand.choice(upgrade_list)
  upgrade_list.remove(upgrade_pick3)
  upgrade_writer.write("Upgrades:", align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 100)
  upgrade_writer.write("1: " + str(upgrade_pick1), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 50)
  upgrade_writer.write("2: " + str(upgrade_pick2), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 0)
  upgrade_writer.write("3: " + str(upgrade_pick3), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 150)
  upgrade_chosen = str(trtl.textinput("Which upgrade are you choosing?", "Enter 1,2, or 3"))
  while upgrade_chosen not in upgrade_list:
    if upgrade_chosen == "1":
      upgrade_chosen = upgrade_pick1
      break
    elif upgrade_chosen == "2":
      upgrade_chosen = upgrade_pick2
      break
    elif upgrade_chosen == "3":
      upgrade_chosen = upgrade_pick3
      break
    else:
      upgrade_chosen = trtl.textinput("Please choose an upgrade.", "Enter 1,2, or 3")
  if upgrade_chosen == "+1 to weapon damage":
    damage += 1
  elif upgrade_chosen == "+1 ammo to barrel":
    max_ammo_loaded +=1
  elif upgrade_chosen == "+25 health":
    health +=25
  elif upgrade_chosen == "+5 extra ammo every wave":
    ammo_after_wave += 5
  elif upgrade_chosen == "wave timer increase by 5":
    wave_timer += 5000
  upgrade_list.append(upgrade_pick1)
  upgrade_list.append(upgrade_pick2)
  upgrade_list.append(upgrade_pick3)
  upgrade_writer.clear()

def debuffs():
  global ammo_after_wave, damage, health, max_ammo_loaded, wave_timer, initial_big_enemy_health, initial_small_enemy_health, size_list
  debuff_pick1 = rand.choice(debuff_list)
  debuff_list.remove(debuff_pick1)
  debuff_pick2 = rand.choice(debuff_list)
  debuff_list.remove(debuff_pick2)
  debuff_pick3 = rand.choice(debuff_list)
  debuff_list.remove(debuff_pick3)
  upgrade_writer.write("Upgrades:", align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 100)
  upgrade_writer.write("1: " + str(debuff_pick1), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 50)
  upgrade_writer.write("2: " + str(debuff_pick2), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 0)
  upgrade_writer.write("3: " + str(debuff_pick3), align='center', font=("Arial", 20, "normal"))
  upgrade_writer.goto(0, 150)
  debuff_chosen = str(trtl.textinput("Choose a curse.", "Enter 1,2, or 3"))
  while debuff_chosen not in debuff_list:
    if debuff_chosen == "1":
      debuff_chosen = debuff_pick1
      break
    elif debuff_chosen == "2":
      debuff_chosen = debuff_pick2
      break
    elif debuff_chosen == "3":
      debuff_chosen = debuff_pick3
      break
    else:
      debuff_chosen = trtl.textinput("Choose a curse.", "Enter 1,2, or 3")
  if debuff_chosen == "add small enemy":
    size_list.append("small")
  elif debuff_chosen == "small enemy turns into big enemy":
    added_enemy = size_list.pop(0)
    if added_enemy == "small":
      size_list.append("big")
    if added_enemy == "big":
      size_list.append("big")
      size_list.append("big")
  elif debuff_chosen == "2x small enemy health":
    initial_small_enemy_health *= 2
  elif debuff_chosen == "2x big enemy health":
    initial_big_enemy_health *= 2
  debuff_list.append(debuff_pick1)
  debuff_list.append(debuff_pick2)
  debuff_list.append(debuff_pick3)
  upgrade_writer.clear()

#----------------------------------------------------------#

#------------------Events----------------#
wn.tracer(1)
new_wave()

wn.listen()

wn.onclick(shot_vfx)

wn.onkeypress(reload, "r")

wn.setup(width=500, height=500)
wn.cv._rootwindow.resizable(False, False)
wn.mainloop()