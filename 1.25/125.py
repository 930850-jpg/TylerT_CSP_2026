# Imports
import turtle as trtl
import random as rand
import keyboard as kb
wn = trtl.Screen()

# Initialize Variables
ammo = 10
damage = 1
size_list = ["small", "small", "small", "small", "small"]
health = 100
wave = 1
enemy_list = []

# Initialize Turtles for writing
ammo_counter = trtl.Turtle()
health_counter = trtl.Turtle()
reloader = trtl.Turtle()
wave_counter = trtl.Turtle()

# Functions
def new_enemies():
  global enemy, enemy_list
  for e in size_list:
    enemy = trtl.Turtle(shape="circle")
    enemy_list.append(enemy)















wn.mainloop()