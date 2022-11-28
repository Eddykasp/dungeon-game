from entities import *

class Level1:
  map_tiles = [["F,WT,WL", "F,WT", "F,WT", "F,WT", "F,WT", "F,WT,WR", "F,WL,WT", "F,WT", "F,WT,DR_0", "F,WT,DL_0", "F,WT", "SL,WT,WR"], 
               ["SL,WL,WB", "F,WB", "F,WB", "F",    "F",    "F,WR",    "F,WL",    "F",    "F,DR_1",    "F,DL_1",    "F",    "F,WR"], 
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
               ["SL,WL",   "F",   "F",   "F,WR",   "F,WL,WT","F,WR,WT","F,WL,WT","F,WR,WT","F,WL,WT",   "F,WR,WT"],
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
  map_tiles = [["F,WL,WT", "F,A_0,WT", "F,A_1,WT", "F,A_2,WT","F,A_3,WT","F,WT","F,WR,WT", "F,WL,WT","F,A_in0,WT","F,A_in1,WT", "F,A_in2,WT", "F,WT,WR"],
               ["F,WL", "F,L_0>A_0;XOR_0;AND_0","F,L_1>A_1;XOR_1;AND_1","F,L_2>A_2;XOR_2;AND_2","F,L_3>A_3;OR_2","F","F,DR_1","F,DL_1","F","F", "F","SL,WR"],
               ["F,WL", "F","F","F","F","F","F,WR","F,WL","F","F","F","F,WR"],
               ["F,WB,WL", "F,WB","F,WB","F,WB","F,WB","F,WB","F,WR,WB","F,WL,WB","F,WB","F,WB","F,WB","F,WR,WB"],
               ["F,WT,WL", "F,WT","F,WT","F,WT","F,WT","F,WT","F,WT","F,WT","F,WT","F,WT","F,WT","F,WT,WR"],
               ["F,WL", "F,A_out0","F,A_out1","F,A_out2","F,A_out3","F","F","F","F","F","F","F,WR"],
               ["F,WB,WL", "F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WR,WB"]
              ]
  logic_blocks = ["NOT_1>A_in1;XOR_1;AND_1;A_in2;XOR_2;AND_2", "NOT_0>NOT_1;A_in0;XOR_0;AND_0;AND_01;XOR_01",
                  "XOR_0>AND_01;XOR_01", "AND_0>OR_0", "XOR_01>A_out0;AND_door", "AND_01>OR_0", "OR_0>XOR_11;AND_11",
                  "XOR_1>AND_11;XOR_11", "AND_1>OR_1", "XOR_11>A_out1;AND_door", "AND_11>OR_1", "OR_1>XOR_21;AND_21",
                  "XOR_2>AND_21;XOR_21", "AND_2>OR_2", "XOR_21>A_out2;AND_door", "AND_21>OR_2", "OR_2>A_out3;AND_door",
                  "AND_door>DL_1;DR_1"]
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
  