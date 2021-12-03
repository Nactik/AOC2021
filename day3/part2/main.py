from functools import reduce
import numpy as np

def mostCommon(element):
    return 1 if np.count_nonzero(element) >= len(element)/2 else 0;

def leastCommon(element):
    return 0 if np.count_nonzero(element) >= len(element)/2 else 1;


f = open("data.txt","r");

oxygen=0;
co2=0;

values = np.array([[int(i) for i in line.strip()] for line in f]);
co2Tab = values
oxygenTab = values

for i in range(0,len(values[0])): 

    #On transpose la matrice afin d'avoir le contenu de chaque colonne par ligne
    transposedOxygen = np.transpose(oxygenTab)
    transposedCo2 = np.transpose(co2Tab)

    mostCommonBits = list(map(mostCommon, transposedOxygen));
    leastCommonBits = list(map(leastCommon, transposedCo2));

    oxygenTab = list(filter(lambda a: True if len(oxygenTab)==1 else a[i] == mostCommonBits[i],oxygenTab));
    co2Tab = list(filter(lambda a: True if len(co2Tab)==1 else a[i] == leastCommonBits[i],co2Tab));

#On repasse les tableau à 1 dimension puisqu'il n'y a plus qu'un résultat
oxygenTab = np.array(oxygenTab).flatten();
co2Tab =  np.array(co2Tab).flatten();

#On transforme le résultat en bin puis en décimal
for i in range(0,len(oxygenTab)):
    power = len(oxygenTab) - 1 -i;
    oxygen += (oxygenTab[i] * (2**power));
    co2 += (co2Tab[i] * (2**power));


print(f"Output : {oxygen * co2}");

f.close();