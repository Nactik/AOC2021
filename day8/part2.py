from functools import reduce
import numpy as np
from numpy.lib.function_base import digitize

digit = {}

decodeKey = {
    'a' : '',
    'b' : '',
    'c' : '',
    'd' : '',
    'e' : '',
    'f' : '',
    'g' : '',
}

def decriptKey(data):
    global decodeKey;
    global digit;

    onlyDigit = np.append(data[0:3],data[-1])
    for number, element in enumerate(onlyDigit) :
        value = 0;
        if number == 0 : # C'est le chiffre un
                decodeKey['c'] = element[0];
                decodeKey['f'] = element[1];
                for letter in element :
                    value += ord(letter)
                digit[1] = value
        if number == 1 : # C'est le chiffre sept
                for letter in element :
                    value += ord(letter)
                
                digit[7] = value
                aDigit = chr(value - digit[1]);
                decodeKey['a'] = aDigit;
        if number == 2 : # C'est le chiffre quatre
                for letter in element :
                    value += ord(letter)
                    if(letter != decodeKey['c'] or letter != decodeKey['f']):
                        decodeKey['b'] += letter;
                        decodeKey['d'] += letter;
                
                digit[4] = value
        if number == 3 : # C'est le chiffre huit
                for letter in element :
                    value += ord(letter)
                
                digit[8] = value
                decodeKey['a'] = aDigit;


    for number, element in enumerate(data[3,9]) :
        value = 0;
        
                
        #if number == 1: # C'est le chiffre 7


f = open("input/test.txt","r");

count = 0

for line in f :
    data = line.split(" | ")[0].strip().split(" ")

    sortedData = np.array(sorted(data,key=lambda element: len(element)));
    decriptKey(sortedData)

print(f"Output : {count} ")

f.close()