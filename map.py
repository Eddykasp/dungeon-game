from tiles import *

"""
A grid containing the map tiles. The tile of certain coordinates can be accessed using the map.
"""
class Map:
  def __init__(self, width, height, tile_width):
    self.tiles = [[Tile(col_index, row_index) for row_index in range(int(height / tile_width))] for col_index in range(int(width / tile_width))]
    #print(len(self.tiles))

    #self.tiles[3][5].color = 4

  def draw(self):
    for row in self.tiles:
      for tile in row:
        tile.draw()

  def get_tile(self, x, y):
    try:
      return self.tiles[int(x / TILE_WIDTH)][int(y / TILE_WIDTH)]
    except:
      return Tile(-1,-1)


  """
  Creates a tile according to the passed code.
  """
  def create_tile(self, tile_id: str, row_index, col_index):
    if tile_id == "_":
      return Tile(row_index, col_index)
    elif tile_id == "F":
      return Floor(row_index, col_index)
    elif tile_id == "WR":
      return WallRight(row_index, col_index)
    elif tile_id == "WL":
      return WallLeft(row_index, col_index)
    elif tile_id == "WB":
      return WallBottom(row_index, col_index)
    elif tile_id == "WT":
      return WallTop(row_index, col_index)
    else:
      return Tile(row_index, col_index)

  def load_map(self,map_spec):
    for col_index in range(len(map_spec)):
      for row_index in range(len(map_spec[col_index])):
        tile_spec = map_spec[col_index][row_index].split(",")
        tile_stack_list = []
        for tile in tile_spec:
          tile_stack_list.append(self.create_tile(tile, row_index, col_index))
        self.tiles[row_index][col_index] = TileStack(row_index, col_index, tile_stack_list)