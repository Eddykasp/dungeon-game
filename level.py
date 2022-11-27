from entities import *

class Level1:
  map_tiles = [["F,WT,WL", "F,WT", "F,WT", "F,WT", "F,WT", "F,WT,WR", "F,WL,WT", "F,WT", "F,WT,DR_0", "F,WT,DL_0", "F,WT", "F,WT,WR"], 
               ["F,WL,WB", "F,WB", "F,WB", "F",    "F",    "F,WR",    "F,WL",    "F",    "F,DR_1",    "F,DL_1",    "F",    "F,WR"], 
               ["F,WL,WT", "F,WT", "F,WR,WT", "F,WL,SP_0", "F,SP_1", "F,WR,SP_2", "F,WL", "F", "F,WR", "PP_2,F,SP_2,WL", "PP_2,F,SP_2", "PP_2,F,SP_2,WR"],
               ["F,WL",    "F",    "F,WR",    "F,WL,SP_3", "F,SP_4", "F,WR,SP_5", "F,WL", "F,L_0>DR_0;DL_0;DR_1;DL_1", "F,WR", "PP_2,F,SP_2,WL", "PP_2,F,SP_2", "PP_2,F,SP_2,WR"],
               ["F,WL",    "F",    "F,WR",    "F,WL,SP_6", "F,SP_7", "F,WR,SP_8", "F,WL", "F", "F,WR", "PP_2,F,SP_2,WL", "PP_2,F,SP_2", "PP_2,F,SP_2,WR"],
               ["F,WL", "F", "F", "F", "F", "F", "F", "F", "F,WR", "F,WL", "F", "F,WR"],
               ["F,WL,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WR,WB", "F,WL,WB", "F,WB", "F,WR,WB"]]
  logic_blocks = ["NOT_0>T_0", "T_0>NOT_1", "T_0>SP_0;SP_1;SP_2;SP_6;SP_7;SP_8", "NOT_1>SP_3"]
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
  