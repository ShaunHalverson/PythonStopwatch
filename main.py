import time
import sys
import select

class Stopwatch:
  def __init__(self):
    self.startTime = None
    self.elapsedTime = 0
    self.isRunning = False

  def startWatch(self):
    if not self.isRunning:
      self.startTime = time.time()
      self.isRunning = True
      print("Stopwatch has started")

  def stopWatch(self):
    if self.isRunning:
      self.elapsedTime = time.time() - self.startTime
      self.isRunning = False
      print("Stopwatch has stopped")

  def resetWatch(self):
    self.elapsedTime = 0
    self.isRunning = False
    print("Stopwatch has been reset")

  def logWatchTime(self):
    totalTime = self.elapsedTime
    if self.isRunning:
      totalTime += time.time() - self.startTime
    print(f"Time: {totalTime:.2f} seconds")


stopwatch = Stopwatch()

while True:
  command = input("Please enter one of the following commands...\nStart\nStop\nReset\nQuit\n\n>")
  if(command == "Start"):
    stopwatch.startWatch()
  elif(command == "Stop"):
    stopwatch.stopWatch()
  elif(command == "Reset"):
    stopwatch.resetWatch()
  elif(command == "Quit"):
    break
  else:
    print("Invalid command. Please try again.")

  while stopwatch.isRunning:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
      break
    stopwatch.logWatchTime()
    time.sleep(1)
