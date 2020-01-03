import math
import base26


def getRanges(strLen, numOfServers):
    # first we genrate the strings:
    startStr = ""
    endStr = ""
    for i in range(strLen):
        startStr += 'a'
        endStr += 'z'

    # then we will convert them into decimal numbers range
    startIndex = base26.base_alphabet_to_10(startStr)
    endIndex = base26.base_alphabet_to_10(endStr)
    step = math.floor((endIndex - startIndex) / numOfServers)

    # and finaly, we will generate list of string indexes:
    tempInd = startIndex
    rangesList = []

    for i in range(numOfServers - 1):
        rangesList.append([base26.base_10_to_alphabet(tempInd),
                           base26.base_10_to_alphabet(tempInd + step)])
        tempInd += step
        tempInd += 1

    rangesList.append([base26.base_10_to_alphabet(tempInd),
                       base26.base_10_to_alphabet(endIndex)])
    return rangesList


"""
mylist = getRanges(6, 99)

for tupple in mylist:
    print(tupple)
"""
