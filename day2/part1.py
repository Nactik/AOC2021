def intrepret_command( command :str, value:int):
    global horizontal;
    global depth;

    if command == "forward" :
        horizontal += value;
    elif command == "down" :
        depth += value;
    elif command == "up" :
        depth -= value;


f = open("input/data.txt","r");
depth = 0;
horizontal = 0;

for line in f : 

    (command, value) = tuple(line.split(' '));
    intrepret_command(command,int(value));


print(f"Output : {depth * horizontal}");

f.close();

