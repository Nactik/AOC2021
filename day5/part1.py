import numpy as np
import re 

f = open("input/data.txt",'r');

diagram = np.zeros((1000,1000),dtype=int);

# On rempli le tableau
for line in f:
    (col1,row1,col2,row2) = tuple([int(i) for i in re.split(" -> |,",line.strip())]);
    
    if(row1 == row2) :
        #On inverse si x1 > x2
        if (col1 > col2):
            diagram[row1,col2:col1+1] += 1; 
        else : 
            diagram[row1,col1:col2+1] += 1;
    if(col1 == col2) :
        if(row1 > row2) :
            diagram[row2:row1+1,col1] += 1;
        else:
            diagram[row1:row2+1,col1] += 1;

print(diagram)
print(f"Ouput : {np.count_nonzero(diagram >= 2)}")

f.close();