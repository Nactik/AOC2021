import numpy as np
f = open("input/data.txt","r");

fishTab = np.array([int(i) for i in f.readline().split(',')])
nbDays = 256;


for i in range(0,nbDays):
    nbZero = np.count_nonzero(fishTab == 0)
    if(nbZero > 0):
        for j in range(0,nbZero):
            fishTab = np.append(fishTab,9);
    fishTab -= 1;
    fishTab = np.where(fishTab < 0,6, fishTab)
    

print(f"Output : {len(fishTab)}")
        

    

f.close()