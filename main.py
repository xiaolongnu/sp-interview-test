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
    totalpresses = 0 # accumulator variable
    # look up the keypresses based on each letter of the input then add it into totalpresses
    for i in word:
        totalpresses += df['keypresses'].loc[df.letter.values == i].values
    return totalpresses[0]


def q2(word):
    numList = [] # init list to store number keys
    # look up number key based on each letter of the input then append it into numList
    for i in word:
        numList.extend(df['num'].loc[df.letter.values == i].values)

    return "".join(map(str, numList))


def q3(inputnum):
    # return nothing if inputnum is empty
    if not inputnum:
        return

    # get list of letters from 1st number in input
    a =  df['letter'].loc[df.num.values == int(inputnum[0])].values
    
    # iteratively get list of letters based on each number in input then perform permutation
    for i in inputnum[1:]:
        c = []
        # get list of letters
        b =  df['letter'].loc[df.num.values == int(i)].values
        #perform pairwise permutation
        for r in itertools.product(a, b): 
            c.append(r[0] + r[1]) #store results in 'c'
        a = c #save result to 'a'

    return a

def q4(inputnum):
    lst = set( q3(inputnum) ) # get all possible list of words then convert list to set type
    return list( WORDS.intersection(lst) ) # perform intersection with words dictionary then return result in list format. 


# entry point of the program
if __name__ == "__main__":
    # should santize the args or not use eval function for production, to prevent execution of arbitrary codes
    print eval(sys.argv[1]+'("'+sys.argv[2]+'")')