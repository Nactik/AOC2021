from functools import reduce
import numpy as np

f = open("input/test.txt","r");

count = 0;
board = [];

for idx,line in enumerate(f) :
    row = [int(i) for i in line.strip()];
    board.append(row);

board = np.array(board);

for row in range(0,len(board)) :
    for col in range(0,len(row)):
        element = board[row,col];
        right = None,
        left = None,
        up = None,
        down = None
        if col != 0 :
            left = board[row,col-1];
        elif col != len(row) -1:
            right = board[row,col+1];
        elif row != 0 :
            up = board[row-1,col];
        elif row != len()
            
            


print(f"Output : {count} ");

f.close()