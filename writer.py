import sys
import re

class Writer():

  def __init__(self):
    self.arg_items = list()

  def get_args(self):
    [self.arg_items.append(arg) for arg in sys.argv[1:]]
    self.arg_items.sort()

  def write_items(self):
    with open('current-items.txt', 'a') as file:
      [file.write(' - ' + item + '\n') for item in self.arg_items]
