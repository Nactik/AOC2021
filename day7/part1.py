from functools import reduce
import sys
f = open("input/data.txt","r");

crabPos = [int(i) for i in f.readline().split(",")];
fuelCost = sys.maxsize;

for i in range(0,max(crabPos)):
    costTab = list(map(lambda a: abs(a-i), crabPos))
    cost = reduce(lambda a,b: a+b,costTab);
    if(cost < fuelCost): fuelCost = cost;

print(f"Output : {fuelCost}")


f.close()