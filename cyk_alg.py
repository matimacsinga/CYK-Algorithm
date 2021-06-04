from itertools import combinations


def cartesianProduct(firstSet, secondSet):
    
    cartProd = list()
    if firstSet == []:
        return secondSet
    elif secondSet == []:
        return firstSet
    else:
        for f in firstSet:
            for s in secondSet:
                cartProd.append(f+s)
    return cartProd

def createProductionRules(filename):
    rules = dict()
    f = open(filename,"r")
    lines = f.readlines()
    for line in lines:
        left, right = line.split("->")
        right = right.rstrip("\n")
        l = right.split("|")
        rules.update({left: l})
    return rules

def readInput(filename):
    f = open(filename,"r")
    i = f.read()
    return i.rstrip("\n")

def createSubwords(wordInput):
    substring = dict()
    for i, j in combinations (range(len(wordInput) + 1), r = 2):
        if(wordInput[i:j] not in substring):
                substring.update({wordInput[i:j]: []})
    return substring

def cykAlgorithm(productionRules,wordInput):
    substring = createSubwords(wordInput)
    for key in substring:
        if len(key) == 1:
            for rule in productionRules:
                if key in productionRules[rule]:
                    substring[key].append(rule)
    for i in range(2,len(wordInput)+1):
        for key in substring:
            if len(key) == i:
                for j in range(0, len(key)-1):
                    prod = cartesianProduct(substring[key[0:j+1]],substring[key[j+1:len(key)]])
                    for sub in prod:
                        for rule in productionRules:
                            if sub in productionRules[rule]:
                                if rule not in substring[key]:
                                    substring[key].append(rule)
    print(substring)
    if 'S' in substring[wordInput]:
        print("Grammar can generate the word!")
    else:
        print("Grammar cannot generate the word.")                                
    




productionRules = createProductionRules("grammar.txt")
wordInput = readInput("word.txt")
#substringDict = createSubwords(wordInput)
cykAlgorithm(productionRules,wordInput)
