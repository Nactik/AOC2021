f = open('data.txt','r')
previous_line = None
count = 0

for line in f :
    current_value = int(line)
    if(previous_line != None): 
        if(current_value > previous_line):
            count += 1
    previous_line = current_value 

print(count)

f.close()