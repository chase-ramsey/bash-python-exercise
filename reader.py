import sys
import re

class Reader():

  def __init__(self):
    self.file = open(sys.argv[1] + '.txt')
    self.items = list()

  def concat_items(self):
    [self.items.append(item[:-1]) for item in self.file]
    self.items = [re.sub(r'\s', '_', item) for item in self.items]
    items_string = (' ').join(self.items)
    return items_string

reader = Reader()
print(reader.concat_items())
