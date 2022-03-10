
import enum
import json
import pandas
import sys 

def convertListToDict(inputList):
    outputDict = {}
    for value in inputList:
        outputDict[value] = 0

    return outputDict


def breakdown(word, symbolsDict):
    if word == "":
        return []
    if len (word) == 1:
        if word in symbolsDict:
           return [word]
        return []
    if len(word) == 2:
        if word in symbolsDict:
            return [word]
        if word[0] in symbolsDict and word[1] in symbolsDict:
            return [word[0], word[1]]
        return []

    breakdowns = [[]]
    if word[0] in symbolsDict:
        breakdowns.append([[word[0]]])
    # elif word[:2] in symbolsDict: 
    #     breakdowns.append([])
    #     breakdowns.append([word[:2]])
    else:
        breakdowns.append([[]])


    for i, letter in enumerate(word[1:], 1):
        onePreviousCombos = breakdowns[i].copy()
        twoPreviousCombos = breakdowns[i-1].copy()
        newCombos = []
        doubleCharPotentialSymbol = word[i-1] + letter

        if letter in symbolsDict:
            if onePreviousCombos == []:
                newCombos.append([letter])
            for combo in onePreviousCombos:
                newCombos.append(combo + [letter])
        
        if doubleCharPotentialSymbol in symbolsDict:

            if twoPreviousCombos == []:
                newCombos.append([doubleCharPotentialSymbol])
            for combo in twoPreviousCombos:
                newCombos.append(combo + [doubleCharPotentialSymbol])
        if newCombos == [] and breakdowns[-1] == [] and i != 1:
            return []

        breakdowns.append(newCombos)
    return breakdowns[-1][-1]

def runBreakdown(word):
    atomicInfoTable = pandas.read_csv("atomic-info.csv")
    symbols = atomicInfoTable.Symbol.values
    for i, s in enumerate(symbols):
        symbols[i] = s.lower()
    
    symbolDict = convertListToDict(symbols)
    # what about the case where there are multiple potential breakdowns?
    return breakdown(word, symbolDict)

def convertListToJson(breakdown):
    output = {"breakdown": breakdown}
    print(json.dumps(output))

breakdown = runBreakdown(sys.argv[1])
convertListToJson(breakdown)
