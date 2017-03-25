import pandas as pd
import os, sys
import itertools

#create keypad dataframe from csv file
df = pd.read_csv("numpad.csv")

#for question 4
#load word dictionary and store the words in a set
with open('WordsRTF.txt') as f:
    lines = f.read().splitlines()
WORDS = set(lines)


def q1(word):
    # look up the keypresses based on each letter of the input then place them in a list
    # when all keypresses are looked up, sum all the keypresses in the list
    x = sum( [df['keypresses'].loc[df.letter.values == i].values for i in word] )
    return x[0]


def q2(word):
    # look up number key based on each letter of the input then append it into numList
    numList = [ df['num'].loc[df.letter.values == i].values[0] for i in word ]
    return "".join(map(str,numList))

def q3(inputnum):
    # get lists of letters from each number in input
    lst = [df['letter'].loc[df.num.values == int(x)].values for x in inputnum]

    # generate permutatations with 'itertools.product'.
    # each permutation is a list, where its then convert to a string with the 'join' function
    return ["".join(r) for r in itertools.product(*lst)]


def q4(inputnum):
    lst = set( q3(inputnum) ) # get all possible list of words then convert list to set type
    return list( WORDS.intersection(lst) ) # perform intersection with words dictionary then return result in list format. 


# entry point of the program
if __name__ == "__main__":
    # should santize the args or not use eval function for production, to prevent execution of arbitrary codes
    print eval(sys.argv[1]+'("'+sys.argv[2]+'")')

