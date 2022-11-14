import pyxel
from tiles import *
from logicTiles import *
from map import *
import random as r
from entities import *

GAME_WIDTH = 160 # 20 Tiles 
GAME_HEIGHT = 112 # 14 Tiles

class Player(Entity):
  def __init__(self):
    self.x = 0
    self.y = 0
    self.speed = 0.5
    self.width = 2
    self.height = 4
    self.wallCollider = True
    self.imageX = [2]
    self.imageY = [0]
    self.health = 3

  def damage(self,damage):
    self.health -= damage
    if (self.health <= 0):
      # TODO: DEATH
      return

class App:
  def __init__(self):
    self.player = Player()
    worm = Worm(5,5)

    self.entities = [worm]

    self.map = Map(GAME_WIDTH, GAME_HEIGHT, TILE_WIDTH)

    self.map.load_map([["F,WT,WL",      "F,PP_0>OR_0;A_0;DR_0;DL_0;T_0,WT",    "F,PP_1>OR_0;DEL_0,WR,WT", "F,WL,WT"], 
                       ["F,WL",         "F,WB",                           "F,WR",                    "F,WL"], 
                       ["F,A_0,WB,WL",  "F,A_1,WB,WT",                    "F,A_2,DR_0,DB_0",         "F,DL_0"],
                       ["F,WL,WT",      "F,WT",                           "F,DT_0",                  "F"]],
                       ["AND_0", "OR_0>A_2","NOT_0>T_0", "T_0>DB_0;DT_0", "DEL_0>A_1"])


    # create random map for testing
    tile_types = ["F", "FWR", "FWB", "FWT", "FWL"]
    # for row_index in range(len(self.map.tiles)):
    #   for col_index in range(len(self.map.tiles[row_index])):
    #     self.map.tiles[row_index][col_index] = self.map.create_tile(tile_types[r.randrange(0, len(tile_types))], row_index, col_index)
      
    pyxel.init(GAME_WIDTH, GAME_HEIGHT, title="Dungeon Game", display_scale=8)
    # load resource file
    pyxel.load("./assets/dungeon_assets.pyxres", image=True, sound=True, music=True)
    self.playingMusic = False
    pyxel.run(self.update, self.draw)

  def update(self):
    if not self.playingMusic:
      pyxel.playm(2,loop=True)
      self.playingMusic = True

    # update entities
    for entity in self.entities:
      if entity.wallCollider:
        collision = self.map.get_tile(entity.x, entity.y).collision(entity.x % TILE_WIDTH, entity.y % TILE_WIDTH, entity.width, entity.height)
        for otherEntity in self.entities:
          if isinstance(otherEntity, CollidingEntity) and otherEntity != entity:
            entityCollision = otherEntity.collision(entity.x, entity.y, entity.width, entity.height)
            entity.update(entityCollision)
        entity.update(collision)
      else:
        entity.update()

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

    self.player.update(player_collision, player_movement)
    # limited fov
    # pyxel.clip(self.player.x - 5, self.player.y - 5, 10, 10)


    self.map.evaluateLogic()

  def draw(self):
    pyxel.cls(0)
    self.map.draw()
    for entity in self.entities:
      entity.draw()
    self.player.draw()

App()