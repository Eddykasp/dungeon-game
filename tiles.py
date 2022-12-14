import pyxel

TILE_WIDTH = 8

class Tile:
  imageId = 0 # all tiles saved on image 0
  imageX = [7] # empty tile marker
  imageY = [0]
  state = 0
  
  def __init__(self, x, y,name="TILE"):
    self.x = x
    self.y = y
    self.name = name

  def draw(self):
    pyxel.blt(self.x* TILE_WIDTH,self.y* TILE_WIDTH,
      pyxel.image(self.imageId),
      self.imageX[self.state] * TILE_WIDTH,
      self.imageY[self.state] * TILE_WIDTH,TILE_WIDTH,TILE_WIDTH,0)

  """
  Returns an int pair to indicate the collision direction, to apply ontop of movement to undo it"""
  def collision(self,sub_tile_x, sub_tile_y, width, height,app):
    return (0,0)

  def interact(self):
    return

class TileStack(Tile):
  def __init__(self, x, y, tiles):
    self.x = x
    self.y = y 
    self.tiles = tiles

  def draw(self):
    for tile in self.tiles:
      tile.draw()

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
    total_collision = [0,0]
    for tile in self.tiles:
      collision = tile.collision(sub_tile_x, sub_tile_y, width, height, app)
      for i in range(len(collision)):
        # highest tile has collision precedence
        if collision[i] != 0 and total_collision[i] != collision[i]:
          total_collision[i] = collision[i]
    return total_collision
  
  def interact(self):
    for tile in self.tiles:
      tile.interact()
        

class Floor(Tile):
  imageX = [2]
  imageY = [0]

class DeathFloor(Tile):
  imageX = [2]
  imageY = [2]  

class Stair(Tile):
  def __init__(self, x, y, name, level_id):
    self.level_id = level_id
    super().__init__(x, y, name)

  def collision(self, sub_tile_x, sub_tile_y, width, height, app):
      app.levelComplete = True
      app.level_id = self.level_id
      return super().collision(sub_tile_x, sub_tile_y, width, height, app)     

class StairRight(Stair):
  imageX = [6]
  imageY = [0] 

class StairLeft(Stair):
  imageX = [5]
  imageY = [0]

class DeathStair(Stair):
  imageX = [3]
  imageY = [2]  

class Wall(Tile):
  thickness = 1

class WallRight(Wall):
  imageX = [0]
  imageY = [0]

  def collision(self,sub_tile_x, sub_tile_y, width, height,app):
    if sub_tile_x + width / 2 > TILE_WIDTH - self.thickness:
      return (-1, 0)
    else:
      return (0,0)

class DeathWallRight(WallRight):
  imageX = [0]
  imageY = [2]    

class WallLeft(Wall):
  imageX = [1]
  imageY = [1]
  
  def collision(self,sub_tile_x, sub_tile_y, width, height,app):
    if sub_tile_x - width / 2 < self.thickness:
      return (1, 0)
    else:
      return (0,0)

class DeathWallLeft(WallLeft):
  imageX = [1]
  imageY = [3]

class WallTop(Wall):
  imageX = [0]
  imageY = [1]

  def collision(self,sub_tile_x, sub_tile_y, width, height,app):
    if sub_tile_y - height / 2 < self.thickness:
      return (0, 1)
    else:
      return (0,0)

class DeathWallTop(WallTop):
  imageX = [0]
  imageY = [3]

class WallBottom(Wall):
  imageX = [1]
  imageY = [0]

  def collision(self,sub_tile_x, sub_tile_y, width, height,app):
    if sub_tile_y + height / 2 > TILE_WIDTH - self.thickness:
      return (0, -1)
    else:
      return (0,0)

class DeathWallBottom(WallBottom):
  imageX = [1]
  imageY = [2]