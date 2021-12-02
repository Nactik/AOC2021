from functools import reduce

f = open('data.txt','r')
output = 0
count1 = 0
count2 = 0

values = [int(line) for line in f]


for i in range(0,len(values)-3):

    count1 = reduce(lambda a,b : a+b, values[i:i+3])
    count2 = reduce(lambda a,b : a+b, values[i+1:i+4])

    if(count2 > count1) : output +=1

print(output)

f.close()