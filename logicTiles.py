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
      pyxel.play(3,self.sound)

  def deactivate(self):
    if (self.state == 1):
      self.state = 0
      self.outputSignal = False


class PressurePlate(Sensor):
  imageX = [3,4]
  imageY = [0,0]

  def collision(self,sub_tile_x, sub_tile_y, width, height, app):
    if sub_tile_x >= 2 and sub_tile_x <= 5\
      and sub_tile_y >= 2 and sub_tile_y <= 5:
      self.activate()
    else:
      self.deactivate()
    return (0,0)

class Lever(Sensor):
  imageX = [3,4]
  imageY = [0,0]

  def interact(self):
    if self.state == 0:
      self.activate()
    else:
      self.deactivate()

class SpikeTrap(Actuator):
  imageX = [5,6]
  imageY = [1,1]

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    if app.playerVulnerable and self.state == 1:
      app.player.damage(1)
    return super().collision(sub_tile_x, sub_tile_y, width, height, app)

class DoorRight(Actuator, WallRight):
  imageX = [0]
  imageY = [0]

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    if self.state == 0:
      return super().collision(sub_tile_x, sub_tile_y, width, height, app)
    else:
      return [0,0]

  def draw(self):
    if self.state == 0:
      super().draw()

class DoorLeft(Actuator, WallLeft):
  imageX = [1]
  imageY = [1]

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    if self.state == 0:
      return super().collision(sub_tile_x, sub_tile_y, width, height, app)
    else:
      return [0,0]

  def draw(self):
    if self.state == 0:
      super().draw()

class DoorTop(Actuator, WallTop):
  imageX = [0]
  imageY = [1]

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    if self.state == 0:
      return super().collision(sub_tile_x, sub_tile_y, width, height, app)
    else:
      return [0,0]

  def draw(self):
    if self.state == 0:
      super().draw()

class DoorBottom(Actuator, WallBottom):
  imageX = [1]
  imageY = [0]

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    if self.state == 0:
      return super().collision(sub_tile_x, sub_tile_y, width, height, app)
    else:
      return [0,0]

  def draw(self):
    if self.state == 0:
      super().draw()
