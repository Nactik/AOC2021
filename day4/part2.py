from functools import reduce
import numpy as np

def sumPositive(a,b) :
    if(a>=0 and b>=0) :
        return a+b;
    elif(a>=0 and b<0) : 
        return a;
    elif(a<0 and b>=0) :
        return b;
    return 0;

f = open("input/data.txt","r");

boards = [];
nbBoardWon = 0;

#Liste des nombres tirés au hasard
drawed = [int(i) for i in f.readline().split(',')];

#Tableau contenant le contenu de chaque board dans chaque case
boardData = f.read().strip().split("\n\n");

#On rempli le tableau de board
for index, board in enumerate(boardData): 
    boards.append([]);
    for boardLine in board.splitlines():
        boards[index].append([int(number) for number in boardLine.split()]);

boards = np.array(boards);
nbBoards = len(boards)

for number in drawed :
    idxBoard = 0;
    while idxBoard < len(boards):
        board = boards[idxBoard];
        for line in board :
            for index, currentNb in enumerate(line):
                if currentNb == number :
                    line[index] = -1; #Si le numéro apparait, on le marque en le mettant à -1

        #On check si la board contient au moins une ligne ou une colonne complete
        boardToEvaluate = board == -1;
        if (any([line.all() for line in boardToEvaluate])) or any([boardToEvaluate[:,i].all() for i in range(0,len(boardToEvaluate[0]))]):
            nbBoardWon +=1
            #Si c'est le dernier à gagner
            if (nbBoardWon == nbBoards): 
                unmarkedSum = reduce(sumPositive ,board.flatten()); 
                print(f"Ouput = {number * unmarkedSum}");
                f.close();
                exit();
            boards = np.delete(boards,idxBoard,0);
        else : 
            # Il ne faut pas incrémenté lorque qu'on supprime puisque le prochain board va prendre la place du board courant
            idxBoard += 1;
            
f.close();