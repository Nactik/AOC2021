from functools import reduce
import numpy as np

def isUniqueNumber(element):
    nbSegment = len(element);
    return nbSegment == 2 or nbSegment == 4 or nbSegment == 3 or nbSegment == 7;

f = open("input/data.txt","r");

count = 0

for line in f :
    output = line.split(" | ")[1].strip().split(" ")
    
    uniqueNumber = np.array(list(map(isUniqueNumber,output)))
    count += np.count_nonzero(uniqueNumber)

print(f"Output : {count} ")

f.close()