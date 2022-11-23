from entities import *

class Level1:
  map_tiles = [["F,WT,WL,WB",   "F,WT",      "F,WR,WT",  "F,WL,WT", "F,WT,DR_0,L_0>DR_0;DL_0",  "F,WT,WR,DL_0"], 
               ["F,WL,WT,WR",   "F,WL",      "F,WR",     "F,WL",    "F,WR",                     "PP_0,F,SP_2,WL,WR"], 
               ["F,WL,WR",      "F,SP_0,WL", "F,WR","F,WL",    "F,WR",                     "F,WL,WR"],
               ["F,WL,WB",      "F,WB",      "F,WB",     "F,WB",    "F,WR,WB",               "SL,WL,WR,WB"]]
  logic_blocks = ["NOT_0>T_1", "T_1>SP_0"]
  player_coords = [3,3]
  def entities(self):
    entities = []
    return entities

class Level2:
  map_tiles = [["F,WL,WT","F,WT","F,WT","F,WT,WR","",       "",       "",       "",       "",""],
               ["F,WL",   "F",   "F",   "F,WR",   "F,WL,WT","F,WR,WT","F,WL,WT","F,WR,WT","F,WL,WT",   "F,WR,WT"],
               ["F,WL",   "F",   "F,L_0","F,DR_0","F,DL_0", "F,DR_1", "F,DL_1", "F,DR_2", "F,DL_2", "F,WR"],
               ["F,WL",   "F",   "F,L_1","F,DR_0","F,DL_0", "F,DR_1", "F,DL_1", "F,DR_2", "F,DL_2", "SL,WR"],
               ["F,WL",   "F",   "F,L_2","F,DR_0","F,DL_0", "F,DR_1", "F,DL_1", "F,DR_2", "F,DL_2", "F,WR"],
               ["F,WL",   "F",   "F",   "F,WR",   "F,WL,WB", "F,WR,WB","F,WL,WB","F,WR,WB","F,WL,WB",   "F,WR,WB"],
               ["F,WL,WB","F,WB","F,WB","F,WR,WB","",        "",       "",       "",       "",""]
               ]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    return entities

class Level3:
  map_tiles = [["F", "F", "F", "SL"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    return entities

class Level4:
  map_tiles = [["F", "F", "F", "F", "SL"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    return entities

class Level5:
  map_tiles = [["F", "F", "F", "F", "F", "SL"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    return entities

class WinLevel:
  map_tiles = [["F", "F", "F", "F", "F"],[]]
  logic_blocks = []
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    entities.append(Worm(60,5))
    entities.append(Worm(5,50))
    return entities

class DeathLevel:
  map_tiles = [["DF,DWL,DWT", "DF,DWT", "DF,DWT", "DF,DWT", "DS,DWT,DWR"],[]]
  logic_blocks = []
  player_coords = [30,3]
  def entities(self):
    entities = []
    return entities
  
class Levels:
  levels = [Level1(), Level2(), Level3(), Level4(), Level5(), WinLevel(), DeathLevel()]
  