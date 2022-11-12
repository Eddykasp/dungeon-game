from sqlite3 import connect
import pyxel
from tiles import *

class Actuator(Tile):
  imageX = [3,4]
  imageY = [1,1]
  name = "Actuator"

  def __init__(self, x, y, name):
      self.name = name
      super().__init__(x,y)

  def __str__(self):
    return self.name + " [" + str(self.state) + "]"
  
  def updateState(self, inputSignal):
    if inputSignal:
      self.state = 1
    else:
      self.state = 0

class Sensor(Tile):
  imageX = [3,4]
  imageY = [0,0]
  sound = [0,0]
  outputSignal = False
  connectTo = []
  name = "Sensor"

  def __init__(self,x,y,name):
    self.name = name
    super().__init__(x,y)

  def __str__(self):
    return self.name + " > " + str(self.connectTo)

  def activate(self):
    if (self.state == 0):
      self.state = 1
      self.outputSignal = True
      pyxel.play(0,self.sound)

  def deactivate(self):
    if (self.state == 1):
      self.state = 0
      self.outputSignal = False


class PressurePlate(Sensor):
  imageX = [3,4]
  imageY = [0,0]

  def collision(self,sub_tile_x, sub_tile_y, width, height):
    if sub_tile_x >= 2 and sub_tile_x <= 5\
      and sub_tile_y >= 2 and sub_tile_y <= 5:
      self.activate()
    else:
      self.deactivate()
    return (0,0)