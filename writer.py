import sys
import re

class Writer():

  def __init__(self):
    self.arg_items = list()
    self.list_name = sys.argv[1]

  def get_args(self):
    [self.arg_items.append(arg) for arg in sys.argv[2:]]
    self.arg_items.sort()
    self.arg_items = [re.sub('_', ' ', item) for item in self.arg_items]

  def write_items(self):
    with open('current-items.txt', 'a') as file:
      file.write(self.list_name.capitalize() + ':\n')
      [file.write('{0}. {1}\n'.format(index + 1, item)) for index, item in enumerate(self.arg_items)]
      file.write('\n')

writer = Writer()
writer.get_args()
writer.write_items()
