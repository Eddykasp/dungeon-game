import pyxel
from tiles import *
from logicTiles import *
from map import *
from entities import *
from level import Levels

GAME_WIDTH = 120 # 15 Tiles 
GAME_HEIGHT = 72 # 9 Tiles
MAX_HEALTH = 1

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
    self.health = MAX_HEALTH

  def damage(self,damage):
    if self.iFrames == 0:
      self.iFrames = 15
      self.health -= damage
      pyxel.play(2,15)
      if (self.health <= 0):
        pass
  
  def draw(self):
    super().draw()
    # HEALTH BAR
    heart_pos = [GAME_WIDTH - 8, 3]
    for i in range(self.health):
      # draw heart
      # pyxel.rect(heart_pos[0] - 1, heart_pos[1] - 2, 7, 7, 0)
      pyxel.rect(heart_pos[0], heart_pos[1], 5, 2, 8)
      pyxel.rect(heart_pos[0] + 1, heart_pos[1] + 2, 3, 1, 8)
      pyxel.rect(heart_pos[0] + 2, heart_pos[1] + 3, 1, 1, 8)
      pyxel.rect(heart_pos[0] + 1, heart_pos[1] - 1, 1, 1, 8)
      pyxel.rect(heart_pos[0] + 3, heart_pos[1] - 1, 1, 1, 8)
      heart_pos[0] -= 9



class App:
  def __init__(self):
    self.player = Player()
    self.levelCounter = 0
    self.levelComplete = False
    self.playerVulnerable = False

    #self.map.load_map([["F,WT,WL",      "F,PP_0>OR_0;A_0;DR_0;DL_0;T_0,WT",    "F,PP_1>OR_0;DEL_0,WR,WT", "F,WL,WT"], 
    #                   ["F,WL",         "F,WB",                           "F,WR",                    "F,WL"], 
    #                   ["F,A_0,WB,WL",  "F,A_1,WB,WT",                    "F,A_2,DR_0,DB_0",         "F,DL_0"],
    #                   ["F,WL,WT",      "F,WT",                           "F,DT_0",                  "F"],
    #                   ["F", "F", "SR", "F"]],
    #                   ["AND_0", "OR_0>A_2","NOT_0>T_0", "T_0>DB_0;DT_0", "DEL_0>A_1"])

    self.loadLevel()
      
    pyxel.init(GAME_WIDTH, GAME_HEIGHT, title="Dungeon Game", display_scale=12)
    # load resource file
    pyxel.load("./assets/dungeon_assets.pyxres", image=True, sound=True, music=True)
    self.playingMusic = False
    pyxel.run(self.update, self.draw)

  def loadLevel(self):
    level = Levels.levels[self.levelCounter]
    self.map = Map(GAME_WIDTH, GAME_HEIGHT, TILE_WIDTH)
    self.map.load_map(level.map_tiles, level.logic_blocks)     
    self.player.x = level.player_coords[0]
    self.player.y = level.player_coords[1]    
    self.entities = level.entities()  

  def update(self):
    if not self.playingMusic:
      pyxel.playm(2,loop=True)
      self.playingMusic = True
    
    if self.player.health <= 0:
      self.levelCounter = -1
      self.loadLevel()
      self.levelComplete = False
      self.player.health = MAX_HEALTH

    if self.levelComplete:
      self.levelCounter += 1
      self.loadLevel()
      self.levelComplete = False

    # entities shouldn't activate the same triggers as the player so for now just disable them
    # for entity in self.entities:
    #   if entity.wallCollider:
    #     collision = self.map.get_tile(entity.x, entity.y).collision(entity.x % TILE_WIDTH, entity.y % TILE_WIDTH, entity.width, entity.height,self)
    #     entity.update(collision)
    #   else:
    #     entity.update()
    for entity in self.entities:
      entity.update([0,0])

    self.playerVulnerable = True
    player_collision = self.map.get_tile(self.player.x, self.player.y).collision(self.player.x % TILE_WIDTH, self.player.y % TILE_WIDTH, self.player.width, self.player.height, self)
    self.playerVulnerable = False
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
    if pyxel.btnp(pyxel.KEY_E):
      self.map.get_tile(self.player.x, self.player.y).interact()

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

    # tutorial text
    pyxel.rect(0,63,120,9,7)
    pyxel.rect(0,64,120,7,0)
    pyxel.text(7,65,"W,A,S,D: move | E: interact",7)

App()