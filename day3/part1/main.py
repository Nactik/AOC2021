from functools import reduce
import numpy as np

def mostCommon(element):
    return 1 if np.count_nonzero(element) > len(element)/2 else 0;

def leastCommon(element):
    return 0 if np.count_nonzero(element) > len(element)/2 else 1;


f = open("data.txt","r");

gamma=0;
epsilon=0;

values = np.array([[int(i) for i in line.strip()] for line in f]);

#On transpose la matrice afin d'avoir le contenu de chaque colonne par ligne
mostCommonBits = list(map(mostCommon, np.transpose(values)));
leastCommonBits = list(map(leastCommon, np.transpose(values)));

#On transforme le résultat en bin puis en décimal
for i in range(0,len(mostCommonBits)):
    power = len(mostCommonBits) - 1 -i;
    gamma += (mostCommonBits[i] * (2**power));
    epsilon += (leastCommonBits[i] * (2**power));



print(f"Output : {gamma * epsilon}");

f.close();