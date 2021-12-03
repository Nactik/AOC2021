from functools import reduce
import numpy as np


f = open("test.txt","r");

values = [[int(i) for i in line.strip()] for line in f]




f.close()