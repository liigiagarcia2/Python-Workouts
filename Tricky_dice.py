#!/usr/bin/env python3

import random

class Dice():

  def __init__(self,tri,side=6):
    self.sides= side
    self.tricky = tri

  def roll_dice(self): # roll dice 10 times for each run
    lr = []
    for _ in range(1,10):
      n = random.randint(1,self.sides)
      
      if self.tricky == True:
        n = random.randint(self.sides-2,self.sides)

      lr.append(n)
    
    return lr
    
    
d1 = Dice(False)  #  regular 6 sided dice
for _ in range(0,5): # 5 run of 10 roll die 
  print(d1.roll_dice())

print("")

d2 = Dice(True,10)  #  tricky 10 sided dice
for _ in range(0,5):
  print(d2.roll_dice())  
  
