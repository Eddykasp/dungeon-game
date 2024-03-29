from entities import *
import random

class Level1:
  map_tiles = [["","","F,WT,WL", "F,WT", "F,WT", "F,WT", "SL_1.1,WT,WR", "F,WL,WT", "F,WT", "F,WT,DR_0", "F,WT,DL_0", "F,WT", "F,WT,WR"], 
               ["","","F,WL,WB", "F,WB", "F",    "F",    "F,WR",    "F,WL",    "F",    "F,DR_1",    "F,DL_1",    "F",    "F,WR"], 
               ["","","F,WL,WT", "F,WR,WT", "F,WL,SP_0", "F", "F,WR,SP_1", "F,WL", "F", "F,WR", "F,SP_5,WL", "PP_0>DEL_0,F,SP_6", "F,SP_7,WR"],
               ["","","F,WL", "F,WR,L_0>DR_0;DL_0;DR_1;DL_1",    "F,WL", "F,SP_2", "F,WR", "F,WL", "F,L_1>DB_0;DT_0;DB_1;DT_1", "F,WR", "F,SP_8,WL", "PP_1>DEL_1,F,SP_9", "F,SP_10,WR"],
               ["","","F,WL,DB_0", "F,WR,DB_1",    "F,WL,SP_3", "F", "F,WR,SP_4", "F,WL", "F", "F,WR", "F,SP_11,WL", "PP_2>DEL_2,F,SP_12", "F,SP_13,WR"],
               ["","","F,WL,DT_0", "F,DT_1", "F", "F", "F", "F", "F", "F,WR", "F,WL", "F", "F,WR"],
               ["","","F,WL,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WB", "F,WR,WB", "F,WL,WB", "F,WB", "SL_2,WR,WB"]]
  logic_blocks = ["NOT_0>T_0", "T_0>SP_0;SP_1;SP_3;SP_4;NOT_1", "NOT_1>SP_2", "NOT_2>NOT_3", "NOT_3>SP_5;SP_7;SP_8;SP_10;SP_11;SP_13",
                 "DEL_0>SP_6", "DEL_1>SP_9", "DEL_2>SP_12"]
  player_coords = [20,5]
  def entities(self):
    entities = []
    return entities

class Level1_1:
  map_tiles = [["", "", "F,WT,WL", "F,WT", "SL_1,WT,WR"],
               ["", "", "F,WL,WB", "F,WB", "F,WB,WR"]]
  logic_blocks = []
  player_coords = [20,5]
  def entities(self):
    entities = []
    return entities

class Level2:
  map_tiles = [["", "F,WL,WT","F,WT","F,WT,WR","","","","","","","","F,WL,WT","F,WT","F,WT,WR"],
               ["", "F,WL","F","F","F,WT,WR","","","","","F,SP_C1,WL,WT","PP_D1,F,SP_D1,WT","PP_E1,F,SP_E1","F","F,WR"],
               ["", "F,WL","F","F","F","F,WT,WR","","F,SP_A2,WL,WT","F,SP_B2,WT","F,SP_C2","F,SP_D2","F,SP_E2","F","F,WR"],
               ["", "F,WL","F","F","F","F","PP_0>OR_0,F,WT,WB","PP_A3>OR_0,F,SP_A3","PP_B3>OR_0,F,SP_B3","PP_C3>OR_1,F,SP_3","PP_D3>OR_2,F,SP_D3","PP_E3>OR_2,F,SP_E3","F","SL_3,WR"],
               ["", "F,WL","F","F","F","F,WB,WR","","F,SP_A4,WL,WB","F,SP_B4,WB","PP_C4>OR_1,F,SP_C4","PP_D4>OR_2,F,SP_D4","F,SP_E4","F","F,WR"],
               ["", "F,WL","F","F","F,WB,WR","","","","","F,SP_C5,WB,WL","F,SP_D5,WB","F,SP_E5","F","F,WR"],
               ["", "F,WL,WB","F,WB","F,WB,WR","","","","","","","","F,WL,WB","F,WB","F,WB,WR"]
               ]
  logic_blocks = ["OR_0>OR_3;OR_4;OR_5;SP_C4;SP_D4",
                  "OR_1>OR_3;OR_4;OR_6",
                  "OR_2>OR_3;OR_5;OR_6",
                  "OR_3>SP_A2;SP_A4;SP_B2;SP_B4;SP_C1;SP_C5;SP_D5;SP_E2;SP_E5",
                  "OR_4>SP_D3;SP_E3",
                  "OR_5>SP_E4",
                  "OR_6>SP_C2;SP_D1;SP_D2;SP_E1"]
  player_coords = [12,28]
  def entities(self):
    entities = []
    return entities

class Level3:
  map_tiles = [["","F,WL,WT", "F,A_0,WT", "F,A_1,WT", "F,A_2,WT","F,A_3,WT","F,WT","F,WR,WT", "F,WL,WT","F,A_in0,WT","F,A_in1,WT", "F,A_in2,WT", "F,WT,WR"],
               ["","F,WL", "F,L_0>A_0;XOR_0;AND_0","F,L_1>A_1;XOR_1;AND_1","F,L_2>A_2;XOR_2;AND_2","F,L_3>A_3;OR_2","F","F,DR_1","F,DL_1","F","F", "F","SL_4,WR"],
               ["","F,WL", "F","F","F","F","F","F,WR","F,WL","F","F","F","F,WR,WB"],
               ["","F,WB,WL", "F,WB","F,WB","F,WB","F,WB","F,WB","F,WR,WB","F,WL,WB","F,WB","F,WB","F,WB,WR"],
               ["","F,WT,WL", "F,WT","F,WT","F,WT","F,WT","F,WT,WR"],
               ["","F,WL,WB", "F,A_out0","F,A_out1","F,A_out2","F,A_out3","F,WR,WB"],
               ["","", "F,WB,WL","F,WB","F,WB","F,WB,WR",]
              ]
  logic_blocks = ["NOT_1>A_in1;XOR_1;AND_1;A_in2;XOR_2;AND_2", "NOT_0>NOT_1;A_in0;XOR_0;AND_0;AND_01;XOR_01",
                  "XOR_0>AND_01;XOR_01", "AND_0>OR_0", "XOR_01>A_out0;AND_door", "AND_01>OR_0", "OR_0>XOR_11;AND_11",
                  "XOR_1>AND_11;XOR_11", "AND_1>OR_1", "XOR_11>A_out1;AND_door", "AND_11>OR_1", "OR_1>XOR_21;AND_21",
                  "XOR_2>AND_21;XOR_21", "AND_2>OR_2", "XOR_21>A_out2;AND_door", "AND_21>OR_2", "OR_2>A_out3;AND_door",
                  "AND_door>DL_1;DR_1"]
  player_coords = [12,5]
  def entities(self):
    entities = []
    return entities

class Level4:
  map_tiles = [["","F,WL,WT,WB", "F,WT", "F,WT", "F,WT","F,WR,WT"],
               ["", "", "F,L_0>OR_f0;OR_f1;OR_f2;OR_f3;NOT_f0,WL"   , "F",      "F",   "F,DR_1", "F,DL_1,SP_0,WR,WT"],
               ["", "", "F,WL,WB", "F,DB_0", "F,WB","F,WB,WR", "F,WL,WR"],
               ["", "", "F,WL,WT", "F,DT_0", "F,WT","F,WT,WR", "F,WL,SP_1,WR"],
               ["", "", "F,WL", "F", "F,L_1>AND_1;OR_f0;OR_f1;NOT_f1;DB_3;DT_3","F,WR", "F,WL,WR"],
               ["", "", "F,WL,WB", "F,DB_3", "F,WB","F,WB,WR", "F,WL,WB,SP_2", "F,WT,WB","F,SP_3,WT,WB","F,WT,WB","F,WT,WB", "SL_WIN,WB,WT,WR"],
               ["", "", "F,WL,WT,L_2>DR_2;DL_2,WB", "F,WB,DT_3", "F,WT,WB","F,WT,DR_2,WB", "F,DL_2,L_3>OR_f0;OR_f2;OR_f4;NOT_f2,WT,WB,WR"]
              ]
  logic_blocks = ["NOT_f0>OR_f4", "NOT_f1>OR_f2;OR_f3;OR_f4", "NOT_f2>OR_f1;OR_f3",
                  "OR_f0>AND_0", "OR_f1>AND_0","OR_f2>AND_0","OR_f3>AND_0","OR_f4>AND_0",
                  "AND_0>DB_0;DT_0", "AND_1>DR_1;DL_1",
                  "NOT_t>T_0", "T_0>SP_0;DEL_0", "DEL_0>SP_1;DEL_1", "DEL_1>SP_2;DEL_2", "DEL_2>SP_3"]
  player_coords = [12,5]
  def entities(self):
    entities = []
    return entities

class WinLevel:
  map_tiles = [["F,WL,WT,A_0", "F,WT","F,WT,A_1","F,WT","F,WT,A_2","F,WT","F,WT,A_3","F,WT","F,WT,A_4","F,WT","F,WT,A_5","F,WT","F,WT,A_6","F,WT","F,WT,WR,A_7"],
               ["F,WL","F,A_8","F","F,A_9","F","F,A_10","F","F,A_11","F","F,A_12","F","F,A_13","F","F,A_14","F,WR"],
               ["F,WL","F","F","F","F","F","F","F","F","F","F","F","F","F","F,WR"],
               ["F,WL","F","F","F","F","F","F","F","F","F","F","F","F","F","F,WR"],
               ["F,WL","F","F","F","F","F","F","F","F","F","F","F","F","F","F,WR"],
               ["F,WL","F","F","F","F","F","F","F","F","F","F","F","F","F","F,WR"],
               ["F,WL","F","F","F","F","F","F","F","F","F","F","F","F","F","F,WR"],
               ["F,WL,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB","F,WB,WR"]]
  logic_blocks = ["NOT_0>T_0","T_0>A_0;A_1;A_2;A_3;A_4;A_5;A_6;A_7;NOT_1","NOT_1>A_8;A_9;A_10;A_11;A_12;A_13;A_14"]
  player_coords = [3,3]
  def entities(self):
    entities = []
    entities.append(Worm(5,5))
    entities.append(Worm(60,5))
    entities.append(Worm(5,50))
    wormcount = 100
    for i in range(wormcount):
      entities.append(Worm(random.random()*120,random.random()*72)) 
    return entities

class DeathLevel:
  map_tiles = [["","","", "", "", "DF,DWL,DWT", "DF,DWT", "DF,DWT", "DF,DWT", "DF,DWT,DWR", "", ""],
               ["","","","", "DF,DWL,DWT", "DF,DWB","DF,DWB","DF","DF,DWB","DF,DWB", "DF,DWT,DWR", ""],
               ["","","","DF,DWL,DWT", "DF,DWR", "", "", "DF,DWL,DWR", "", "", "DF,DWL", "DF,DWT,DWR"],
               ["","","","DF,DWL", "DF","DF,DWT","DF,DWT","DF","DF,DWT","DF,DWT","DF","DF,DWR"],
               ["","","","DF,DWL,DWB","DF","DF","DF","DS_1","DF","DF","DF","DF,DWR,DWB"],
               ["","","","", "DF,DWL", "DF,DWB","DF","DF,DWB","DF","DF,DWB","DF,DWR"],
               ["","","","", "DF,DWL,DWR,DWB", "", "DF,DWL,DWR,DWB", "", "DF,DWL,DWR,DWB", "", "DF,DWL,DWR,DWB"]]
  logic_blocks = []
  player_coords = [60,5]
  def entities(self):
    entities = []
    return entities
  
class Levels:
  levels = {"1": Level1(), "2": Level2(), "3": Level3(), "4": Level4(), 
            "WIN": WinLevel(), "DEATH": DeathLevel(), "1.1": Level1_1()}
  