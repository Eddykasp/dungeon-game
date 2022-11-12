from functools import reduce
from sqlite3 import connect
from unicodedata import name
import pyxel

class LogicGate():
  inputs = []
  outputSignal = False
  connectTo = []

  def __str__(self):
    return str(str(self.inputs) + " -> " + self.name + " > " + str(self.connectTo))

  def __init__(self, name):
    self.name = name

  def updateState(self,inputSignal):
    # just a wire
    self.outputSignal = inputSignal

  def resetTick(self):
    # reset any memorized inputs for next evaluation
    # self.outputSignal = False
    self.inputs = []

class And(LogicGate):
  def updateState(self, inputSignal):
      self.inputs.append(inputSignal)
      self.outputSignal = reduce(lambda a, b: a and b, self.inputs)

class Or(LogicGate):
  def updateState(self, inputSignal):
      self.inputs.append(inputSignal)
      self.outputSignal = reduce(lambda a, b: a or b, self.inputs)

class Not(LogicGate):
  def updateState(self, inputSignal):
      self.inputs = [inputSignal]
      self.outputSignal = not inputSignal

  