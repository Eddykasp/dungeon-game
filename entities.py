import pyxel
import random as r
from tiles import TILE_WIDTH
from map import *

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
  renderDirection = 1

  def __init__(self,x,y):
    self.x = x
    self.y = y

  def draw(self):
    pyxel.blt(self.x - self.width / 2, self.y - self.height / 2, 
      pyxel.image(self.imageId), self.imageX[self.state] * TILE_WIDTH,
      self.imageY[self.state]  * TILE_WIDTH,
      self.width * self.renderDirection, self.height)

  def move(self, movement):
    self.x += movement[0] * self.speed
    self.y += movement[1] * self.speed

  def update(self, collision=[0,0], newDirection=[0,0]):
    self.direction = newDirection
    self.move([self.direction[0] + collision[0], 
               self.direction[1] + collision[1]])
    if self.direction[0] < 0:
      self.renderDirection = -1
    elif self.direction[0] > 0:
      self.renderDirection = 1

class CollidingEntity(Entity):
  def collision(self,x, y, width, height,map:Map,entities):
    return (0,0)

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

class MovableBlock(CollidingEntity):
  imageX = [0]
  imageY = [0]
  width = 4
  height = 4

  def collision(self,x, y, width, height,map:Map,entities):
    def checkOtherCollisions():
      collision = map.get_tile(self.x,self.y).collision(self.x % TILE_WIDTH, self.y % TILE_WIDTH, self.width, self.height)
      entityCollision = [0,0]
      for otherEntity in entities:
          if isinstance(otherEntity, CollidingEntity) and otherEntity != self:
            entityCollision = otherEntity.collision(self.x, self.y, self.width, self.height,map,entities)
            self.update(entityCollision)
      return [collision[0] + entityCollision[0], collision[1] + entityCollision[1]]
      
    # left side
    if x + width / 2 > self.x - self.width / 2 and x < self.x\
      and y >= self.y - self.height / 2 and y <= self.y + height:
        collision = checkOtherCollisions()
        if collision[0] == 0 and collision[1] == 0:
          self.move([1,0])
        return collision
    # right side
    elif x - width / 2 < self.x + self.width / 2 and x > self.x\
      and y >= self.y - self.height / 2 and y <= self.y + height:
      collision = checkOtherCollisions()
      if collision[0] == 0 and collision[1] == 0:
        self.move([-1,0])
      return collision

    # bottom side
    elif y - height / 2 < self.y + self.height / 2 and y > self.y\
      and x >= self.x - self.width / 2 and x <= self.x + width:
        collision = checkOtherCollisions()
        if collision[0] == 0 and collision[1] == 0:
          self.move([0,-1])
        return collision

    # top side
    elif  y + height / 2 > self.y - self.height / 2 and y < self.y\
      and x >= self.x - self.width / 2 and x <= self.x + width:
        collision = checkOtherCollisions()
        if collision[0] == 0 and collision[1] == 0:
          self.move([0,1])
        return collision
    return (0,0)
