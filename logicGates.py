from functools import reduce

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

# trigger an output signal after x ticks, reset if it receives an input signal
class Timer(LogicGate):
  timerResetCounter = 0
  clockSpeed = 20
  def updateState(self, inputSignal):
    if self.timerResetCounter > 0:
      self.timerResetCounter -= 1
      return
    if not inputSignal:
      self.inputs.append(inputSignal)
    elif inputSignal:
      self.inputs = []
    self.outputSignal = False
    if len(self.inputs) > self.clockSpeed:
      self.outputSignal = True
      self.timerResetCounter = self.clockSpeed
      self.inputs = []

  def resetTick(self):
      # do nothing
      return

  