import pandas as pd
import os, sys
import itertools

df = pd.read_csv("numpad.csv")


def q1(word):
    totalpresses = 0
    for i in word:
        totalpresses += df['keypresses'].loc[df.letter.values == i].values
    return totalpresses[0]


def q2(word):
    numList = []
    for i in word:
        numList.extend(df['num'].loc[df.letter.values == i].values)

    return "".join(map(str, numList))


def q3(inputnum):
    if not inputnum:
        return

    a =  df['letter'].loc[df.num.values == int(inputnum[0])].values
    
    for i in inputnum[1:]:
        c = []
        b =  df['letter'].loc[df.num.values == int(i)].values
        for r in itertools.product(a, b): 
            c.append(r[0] + r[1])
        a = c

    return a


with open('WordsRTF.txt') as f:
    lines = f.read().splitlines()
WORDS = set(lines)

def q4(inputnum):
    lst = set( q3(inputnum) )
    return list( WORDS.intersection(lst) )



if __name__ == "__main__":
    print eval(sys.argv[1]+'("'+sys.argv[2]+'")')