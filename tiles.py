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
  def collision(self,sub_tile_x, sub_tile_y) -> bool:
    return (0,0)

class Floor(Tile):
  color = 2
  wall_color = 3

class FloorWallRight(Floor):
  def draw(self):
    super().draw()
    pyxel.rect((self.x * TILE_WIDTH) + TILE_WIDTH - 1, self.y * TILE_WIDTH, 1, TILE_WIDTH, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y):
    if sub_tile_x >= TILE_WIDTH - 2:
      return (-1, 0)
    else:
      return (0,0)

class FloorWallLeft(Floor):
  def draw(self):
    super().draw()
    pyxel.rect(self.x * TILE_WIDTH, self.y * TILE_WIDTH, 1, TILE_WIDTH, self.wall_color)
  
  def collision(self,sub_tile_x, sub_tile_y):
    if sub_tile_x <= 2:
      return (1, 0)
    else:
      return (0,0)

class FloorWallTop(Floor):
  def draw(self):
    super().draw()
    pyxel.rect(self.x * TILE_WIDTH, self.y * TILE_WIDTH, TILE_WIDTH, 1, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y):
    if sub_tile_y <= 2:
      return (0, 1)
    else:
      return (0,0)

class FloorWallBottom(Floor):
  def draw(self):
    super().draw()
    pyxel.rect(self.x * TILE_WIDTH, (self.y * TILE_WIDTH) + TILE_WIDTH - 1, TILE_WIDTH, 1, self.wall_color)

  def collision(self,sub_tile_x, sub_tile_y):
    if sub_tile_y >= TILE_WIDTH - 2:
      return (0, -1)
    else:
      return (0,0)