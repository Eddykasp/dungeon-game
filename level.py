from entities import *

class Level1:
  map_tiles = [["F,WT,WL,WB",   "F,WT",  "F,WR,WT", "F,WL,WT", "F,WT,DR_0,PP_0>DR_0;DL_0", "F,WT,WR,DL_0"], 
               ["F,WL,WT,WR",   "F,WL",  "F,WR",    "F,WL",    "F,WR",                     "F,WL,WR"], 
               ["F,WL,WR",      "F,SP_0,WL",  "F,WR",    "F,WL",    "F,WR",                     "F,WL,WR"],
               ["F,WL,WB",      "F,WB",  "F,WB",    "F,WB",    "F,WB",                  "SR,WR,WB"]]
  logic_blocks = ["NOT_0>NOT_1", "NOT_1>SP_0"]
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    return entities

class Level2:
  map_tiles = [["F", "F", "SR"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    return entities

class Level3:
  map_tiles = [["F", "F", "F", "SR"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    return entities

class Level4:
  map_tiles = [["F", "F", "F", "F", "SR"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    return entities

class Level5:
  map_tiles = [["F", "F", "F", "F", "F"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    return entities
  
class Levels:
  levels = [Level1(), Level2(), Level3(), Level4(), Level5()]
  