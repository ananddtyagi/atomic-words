
import json
import pandas
import sys 

def convertListToDict(inputList):
    outputDict = {}
    for value in inputList:
        outputDict[value] = 0

    return outputDict

def baseCases(word, symbolsDict):
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

def breakdown(word, symbolsDict):
    if baseCases(word, symbolsDict) == []:
        return []
    
    #so now we know, word is greater than 2 letters
    breakdowns = [[]] #we treat 0 not as the corresponding to the 0th value, but empty string. So breakdowns will end up being len(word) + 1 

    if word[0] in symbolsDict:
        breakdowns.append([word[0]])
    else: 
        breakdowns.append([[]])

    [[], []]

    for i, letter in enumerate(word[1:]):
        onePreviousCombos = breakdowns[i].copy()
        twoPreviousCombos = breakdowns[i-1].copy()

        newCombos = []
        doubleCharPotentialSymbol = word[i-1] + letter

        if letter in symbolsDict:
            for combo in onePreviousCombos:
                newCombos.append(onePreviousCombos + [letter])
        
        if doubleCharPotentialSymbol in symbolsDict:
            for combo in twoPreviousCombos:
                newCombos.append(twoPreviousCombos + [doubleCharPotentialSymbol])

        if newCombos == [] and breakdowns[-1] == []:
            return 

        breakdowns += newCombos

    return breakdowns[-1]

def runBreakdown(word):
    atomicInfoTable = pandas.read_csv("atomic-info.csv")
    symbols = atomicInfoTable.Symbol.values
    for i, s in enumerate(symbols):
        symbols[i] = s.lower()
    
    symbolDict = convertListToDict(symbols)
    # what about the case where there are multiple potential breakdowns?
    return breakdown(word, symbolDict)

def convertListToJson(breakdown):
    # if breakdown == []:
    #     print(json.dumps({"breakdown": []}))
    #     return
    output = {"breakdown": breakdown}
    print(json.dumps(output))

breakdown = runBreakdown(sys.argv[1])
convertListToJson(breakdown)
