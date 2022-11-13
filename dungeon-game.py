import pyxel
from tiles import *
from logicTiles import *
from map import *
import random as r
from entities import *

GAME_WIDTH = 160 # 20 Tiles 
GAME_HEIGHT = 112 # 14 Tiles

class Player:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.speed = 1
    self.width = 6
    self.height = 6

  def draw(self):
    pyxel.rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height, 5)
    
  def move(self, movement, collision):
    self.x += (movement[0] + collision[0]) * self.speed
    self.y += (movement[1] + collision[1]) * self.speed

class App:
  def __init__(self):
    self.player = Player()
    worm = Worm(5,5)

    self.entities = [worm]

    self.map = Map(GAME_WIDTH, GAME_HEIGHT, TILE_WIDTH)

    self.map.load_map([["F,WT,WL",      "F,PP_0>OR_0;A_0;DR_0,WT",    "F,PP_1>OR_0;A_1,WR,WT"], 
                       ["F,WL",         "F,WB",                  "F,WR"], 
                       ["F,A_0,WB,WL",  "F,A_1,WB,WT",           "F,A_2,DR_0,WB"]],
                       ["AND_0", "OR_0>A_2"])


    # create random map for testing
    tile_types = ["F", "FWR", "FWB", "FWT", "FWL"]
    # for row_index in range(len(self.map.tiles)):
    #   for col_index in range(len(self.map.tiles[row_index])):
    #     self.map.tiles[row_index][col_index] = self.map.create_tile(tile_types[r.randrange(0, len(tile_types))], row_index, col_index)
      
    pyxel.init(GAME_WIDTH, GAME_HEIGHT, title="Dungeon Game", display_scale=8)
    # load resource file
    pyxel.load("./assets/dungeon_assets.pyxres", image=True, sound=True)
    pyxel.run(self.update, self.draw)

  def update(self):
    player_collision = self.map.get_tile(self.player.x, self.player.y).collision(self.player.x % TILE_WIDTH, self.player.y % TILE_WIDTH, self.player.width, self.player.height)
    #print(player_collision)
    player_movement = [0,0]
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    if pyxel.btnp(pyxel.KEY_RIGHT,hold=1,repeat=1) or pyxel.btnp(pyxel.KEY_D,hold=1,repeat=1):
      player_movement[0] = 1
    if pyxel.btnp(pyxel.KEY_LEFT,hold=1,repeat=1) or pyxel.btnp(pyxel.KEY_A,hold=1,repeat=1):
      player_movement[0] = -1
    if pyxel.btnp(pyxel.KEY_UP,hold=1,repeat=1) or pyxel.btnp(pyxel.KEY_W,hold=1,repeat=1):
      player_movement[1] = -1
    if pyxel.btnp(pyxel.KEY_DOWN,hold=1,repeat=1) or pyxel.btnp(pyxel.KEY_S,hold=1,repeat=1):
      player_movement[1] = 1

    self.player.move(player_movement, player_collision)

    # update entities
    for entity in self.entities:
      if entity.wallCollider:
        collision = self.map.get_tile(entity.x, entity.y).collision(entity.x % TILE_WIDTH, entity.y % TILE_WIDTH, entity.width, entity.height)
        entity.update(collision)
      else:
        entity.update()

    self.map.evaluateLogic()

  def draw(self):
    pyxel.cls(0)
    self.map.draw()
    for entity in self.entities:
      entity.draw()
    self.player.draw()

App()