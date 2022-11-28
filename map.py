from tiles import *
from logicTiles import *
from logicGates import *

"""
A grid containing the map tiles. The tile of certain coordinates can be accessed using the map.
"""
class Map:
  def __init__(self, width, height, tile_width):
    self.tiles = [[Tile(col_index, row_index) for row_index in range(int(height / tile_width))] for col_index in range(int(width / tile_width))]
    self.logicTiles = {}

  def draw(self):
    for row in self.tiles:
      for tile in row:
        tile.draw()

  def get_tile(self, x, y):
    try:
      return self.tiles[int(x / TILE_WIDTH)][int(y / TILE_WIDTH)]
    except:
      return Tile(-1,-1)

  def evaluateLogic(self):
    #print("------------------")
    for tileId in self.logicTiles:
      logicTile = self.logicTiles[tileId]
      if isinstance(logicTile, LogicGate):
        logicTile.resetTick()
    for tileId in self.logicTiles:
      logicTile = self.logicTiles[tileId]
      if not isinstance(logicTile,Actuator):
        try:
          # no sanity checking in logic network, if multiple things are hooked up
          # to the same receiver, the last one wins
          for connection in logicTile.connectTo:
            self.logicTiles[connection].updateState(logicTile.outputSignal)
          #print(str(logicTile) + " " + str(logicTile.outputSignal) + " " + str(self.logicTiles[logicTile.connectTo]))
        except Exception as error:
          f = True
          print(self.logicTiles)
          print(str(logicTile.connectTo) + " is not defined in " + str(logicTile))


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
    elif tile_id == "DS":
      return DeathStair(row_index, col_index)
    elif tile_id == "DF":
      return DeathFloor(row_index, col_index) 
    elif tile_id == "DWR":
      return DeathWallRight(row_index, col_index)  
    elif tile_id == "DWL":
      return DeathWallLeft(row_index, col_index) 
    elif tile_id == "DWT":
      return DeathWallTop(row_index, col_index)
    elif tile_id == "DWB":
      return DeathWallBottom(row_index, col_index)
    elif tile_id.startswith("PP"):
      pressurePlate = PressurePlate(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, pressurePlate)
      return pressurePlate
    elif tile_id.startswith("L"):
      lever = Lever(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, lever)
      return lever
    elif tile_id.startswith("A"):
      actuator = Actuator(row_index, col_index, tile_id)
      self.logicTiles[tile_id] = actuator
      return actuator
    elif tile_id.startswith("DR"):
      door = DoorRight(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, door)
      return door
    elif tile_id.startswith("DL"):
      door = DoorLeft(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, door)
      return door
    elif tile_id.startswith("DT"):
      door = DoorTop(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, door)
      return door
    elif tile_id.startswith("DB"):
      door = DoorBottom(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, door)
      return door
    elif tile_id.startswith("SP"):
      spikeTrap = SpikeTrap(row_index, col_index, tile_id)
      self.id_to_connection(tile_id, spikeTrap)
      return spikeTrap
    elif tile_id == "SR":
      return StairRight(row_index, col_index)
    elif tile_id == "SL":
      return StairLeft(row_index, col_index)  
    else:
      return Tile(row_index, col_index)

  def create_logic_gate(self, gate_id: str):
    if gate_id.startswith("AND"):
      andGate = And(gate_id)
      self.id_to_connection(gate_id, andGate)
    elif gate_id.startswith("OR"):
      orGate = Or(gate_id)
      self.id_to_connection(gate_id, orGate)
    elif gate_id.startswith("NOT"):
      notGate = Not(gate_id)
      self.id_to_connection(gate_id, notGate)
    elif gate_id.startswith("XOR"):
      xorGate = Xor(gate_id)
      self.id_to_connection(gate_id, xorGate)
    elif gate_id.startswith("T"):
      timer = Timer(gate_id)
      self.id_to_connection(gate_id, timer)
    elif gate_id.startswith("DEL"):
      delay = Delay(gate_id)
      self.id_to_connection(gate_id, delay)
    else:
      print(gate_id + " can't be parsed as a logic gate.")

  def id_to_connection(self,logic_id,gate_or_sensor):
    if ">" in logic_id:
      id, targets_str = logic_id.split(">")
      targets = targets_str.split(";")
      gate_or_sensor.connectTo = targets
      self.logicTiles[id] = gate_or_sensor
      gate_or_sensor.name = id
    else:
      self.logicTiles[logic_id] = gate_or_sensor
    

  def load_map(self,map_spec, logic_gates):
    for col_index in range(len(map_spec)):
      for row_index in range(len(map_spec[col_index])):
        tile_spec = map_spec[col_index][row_index].split(",")
        tile_stack_list = []
        for tile in tile_spec:
          tile_stack_list.append(self.create_tile(tile, row_index, col_index))
        self.tiles[row_index][col_index] = TileStack(row_index, col_index, tile_stack_list)
    for gate in logic_gates:
      self.create_logic_gate(gate)

    # for logic in self.logicTiles:
    #   print(self.logicTiles[logic])