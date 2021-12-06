import numpy as np
f = open("input/test.txt","r");

fishTab = [int(i) for i in f.readline().split(',')]
nbDays = 80;



for i in range(0,nbDays):
    nbZero = np.count_nonzero(fishTab == 0)
    if(nbZero > 0):
        for j in range(0,nbZero):
            fishTab.append(9);

        

    

f.close()