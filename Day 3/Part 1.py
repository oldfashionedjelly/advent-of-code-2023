import re
import math 
from collections import defaultdict


total = 0
board = []
gear_nums = defaultdict(list)

def consider_number_neighbors(start_y, start_x, end_y, end_x, num):
  global gear_nums
  for y in range(start_y, end_y+1):
    for x in range(start_x, end_x+1):
      if y >= 0 and y < len(board) and x >= 0 and x < len(board[y]):
        if board[y][x] not in '0123456789.':
          if board[y][x] == '*':
            gear_nums[ (y,x) ].append(num)
          return True
  return False

num_pattern = re.compile('\d+')

for line in open('input.txt').readlines():
  board.append( line.strip() )

for row_num in range(len(board)):
  for match in re.finditer(num_pattern, board[row_num]):
    if consider_number_neighbors(row_num-1, match.start()-1, row_num+1, match.end(), int(match.group(0))):
      total += int(match.group(0))

print(total)
