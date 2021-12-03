def intrepret_command( command :str, val:int):
    global horizontal;
    global depth;
    global aim;

    if command == "forward" :
        horizontal += val;
        depth += (aim * val);
    elif command == "down" :
        aim += val;
    elif command == "up" :
        aim -= val;


f = open("input/data.txt","r");
depth = 0;
horizontal = 0;
aim = 0;

for line in f : 

    (command, value) = tuple(line.split(' '));
    intrepret_command(command,int(value));


print(f"Output : {depth * horizontal}");

f.close();

