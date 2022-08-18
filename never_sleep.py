from enum import Enum
import random
import time
import pyautogui

class Direction(Enum):
  RIGHT = 1
  LEFT = 2
  UP = 3
  DOWN = 4
 
class Direction_Switch:
  def direction(self, direction_enum):
    
    default = pyautogui.move(1, 0)
    
    return getattr(self, 'case_' + str(direction_enum.name), lambda: default)()
  
  def case_RIGHT(self):
    pyautogui.move(1, 0)
    return
  
  def case_LEFT(self):
    pyautogui.move(-1, 0)
    return
  
  def case_UP(self):
    pyautogui.move(0, -1)
    return
  
  def case_DOWN(self):
    pyautogui.move(0, 1)
    return
  
direction_index = 1
direction_switch = Direction_Switch()
  
while True:
  sleep_time = random.randint(10,120)
  time.sleep(sleep_time)
  direction_switch.direction(Direction(direction_index))
  direction_index = random.randint(1,4)
