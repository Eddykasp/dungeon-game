import pyxel

TILE_WIDTH = 20

class Tile:
  color = 1
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    pyxel.rect(self.x * TILE_WIDTH, self.y * TILE_WIDTH, TILE_WIDTH, TILE_WIDTH, self.color)

  """
  Returns an int pair to indicate the collision direction, to apply ontop of movement to undo it"""
  def collision(self,sub_tile_x, sub_tile_y, width, height):
    return (0,0)

class TileStack(Tile):
  def __init__(self, x, y, tiles):
    self.x = x
    self.y = y 
    self.tiles = tiles

  def draw(self):
    for tile in self.tiles:
      tile.draw()

  def collision(self, sub_tile_x, sub_tile_y, width, height):
    total_collision = [0,0]
    for tile in self.tiles:
      collision = tile.collision(sub_tile_x, sub_tile_y, width, height)
      for i in range(len(collision)):
        # highest tile has collision precedence
        if collision[i] != 0 and total_collision[i] != collision[i]:
          total_collision[i] = collision[i]
    return total_collision
        

class Floor(Tile):
  color = 2

class Wall(Tile):
  wall_color = 3
  thickness = 2

class WallRight(Wall):
  def draw(self):
    pyxel.rect((self.x * TILE_WIDTH) + TILE_WIDTH - self.thickness, self.y * TILE_WIDTH, self.thickness, TILE_WIDTH, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y, width, height):
    if sub_tile_x + width / 2 >= TILE_WIDTH - self.thickness:
      return (-1, 0)
    else:
      return (0,0)

class WallLeft(Wall):
  def draw(self):
    pyxel.rect(self.x * TILE_WIDTH, self.y * TILE_WIDTH, self.thickness, TILE_WIDTH, self.wall_color)
  
  def collision(self,sub_tile_x, sub_tile_y, width, height):
    if sub_tile_x - width / 2 <= self.thickness:
      return (1, 0)
    else:
      return (0,0)

class WallTop(Wall):
  def draw(self):
    pyxel.rect(self.x * TILE_WIDTH, self.y * TILE_WIDTH, TILE_WIDTH, self.thickness, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y, width, height):
    if sub_tile_y - height / 2 <= self.thickness:
      return (0, 1)
    else:
      return (0,0)

class WallBottom(Wall):
  def draw(self):
    pyxel.rect(self.x * TILE_WIDTH, (self.y * TILE_WIDTH) + TILE_WIDTH - self.thickness, TILE_WIDTH, self.thickness, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y, width, height):
    if sub_tile_y + height / 2 >= TILE_WIDTH - self.thickness:
      return (0, -1)
    else:
      return (0,0)