from functools import reduce
import numpy as np
import sys

f = open("input/data.txt","r");

count = 0;
board = [];

for idx,line in enumerate(f) :
    row = [int(i) for i in line.strip()];
    board.append(row);

board = np.array(board);

for row in range(0,len(board)) :
    for col in range(0,len(board[row])):
        element = board[row,col];
        right = sys.maxsize;
        left = sys.maxsize;
        up = sys.maxsize;
        down = sys.maxsize;
        if col != 0 :
            left = board[row,col-1];
        if col != len(board[row]) -1:
            right = board[row,col+1];
        if row != 0 :
            up = board[row-1,col];
        if row != len(board)-1:
            down = board[row+1,col]

        if element < right and element < left and element < up and element < down : 
            count += (element+1)
            
print(f"Output : {count} ");

f.close()