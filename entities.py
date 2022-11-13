import pyxel
import random as r
from tiles import TILE_WIDTH

# UTILS
def reverseDirection(direction):
  if direction[0] != 0:
    return [direction[0] * -1, direction[1]]
  elif direction[1] != 0:
    return [direction[0], direction[1] * -1]
  else:
    return direction

def turnRight(direction):
  if direction[0] == 1 and direction[1] == 0:
    return [0,1]
  elif direction[0] == 0 and direction[1] == 1:
    return [-1,0]
  elif direction[0] == -1 and direction[1] == 0:
    return [0,-1]
  else:
    return [1,0]

def turnLeft(direction):
  if direction[0] == 1 and direction[1] == 0:
    return [0,-1]
  elif direction[0] == 0 and direction[1] == -1:
    return [-1,0]
  elif direction[0] == -1 and direction[1] == 0:
    return [0,1]
  else:
    return [1,0]


# Entities x, and y are pixel accurate positions at the center of the entitie's bounding box
class Entity:
  direction = [0,0]
  state = 0
  imageId = 1 # entities are on image 1
  speed = 1
  imageX = [0]
  imageY = [0]
  width = 8
  height = 8
  wallCollider = False

  def __init__(self,x,y):
    self.x = x
    self.y = y

  def draw(self):
    pyxel.blt(self.x - self.width / 2, self.y - self.height / 2, 
      pyxel.image(self.imageId), self.imageX[self.state] * TILE_WIDTH,
      self.imageY[self.state]  * TILE_WIDTH,
      self.width, self.height)

  def move(self, movement):
    self.x += movement[0] * self.speed
    self.y += movement[1] * self.speed

  def update(self, collision=[0,0], newDirection=[0,0]):
    self.direction = newDirection
    self.move([self.direction[0] + collision[0], 
               self.direction[1] + collision[1]])

class Worm(Entity):
  width = 3
  height = 1
  wallCollider = True
  collidedLastTick = False
  speed = 0.5

  def draw(self):
    if self.direction[1] != 0:
      pyxel.rect(self.x - self.height / 2, self.y - self.width / 2, self.height, self.width, 4)
    else:
      pyxel.rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height, 4)

  def update(self, collision):
    choice = r.random()
    if self.collidedLastTick:
      choice = choice * 100 / 35
      self.collidedLastTick = False
    if choice < 0.05:
      direction = reverseDirection(self.direction)
    elif choice >= 0.05 and choice < 0.2:
      direction = turnRight(self.direction)
    elif choice >= 0.2 and choice < 0.35:
      direction = turnLeft(self.direction)
    else:
      direction = self.direction
    if collision[0] != 0 or collision[1] != 0:
      self.collidedLastTick = True
    super().update(collision, direction)
