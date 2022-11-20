import json
import numpy as np

def task(jsonString1, jsonString2):
    data = json.loads(jsonString1)
    data2 = json.loads(jsonString2)

    amount = len(data)
    for item in data:
        if isinstance(item, list):
            amount += len(item)-1

    nameToIndex = dict()
    indexToName = dict()

    index = 0
    for item in data:
        if isinstance(item, list):
            for i_item in item:
                nameToIndex[i_item] = index
                indexToName[index] = i_item
                index += 1
        else:
            nameToIndex[item] = index
            indexToName[index] = item
            index += 1

    cluster = dict()
    index = 0
    for item in data:
        if isinstance(item, list):
            for i_item in item:
                cluster[i_item] = index
        else:
            cluster[item] = index
        index += 1

    A = np.zeros((amount, amount))
    B = np.zeros((amount, amount))

    for i in range(amount):
        for j in range(amount):
            if cluster[indexToName[i]] <= cluster[indexToName[j]]:
                A[i][j] = 1

    index = 0
    for item in data2:
        if isinstance(item, list):
            for i_item in item:
                cluster[i_item] = index
        else:
            cluster[item] = index
        index += 1

    for i in range(amount):
        for j in range(amount):
            if cluster[indexToName[i]] <= cluster[indexToName[j]]:
                B[i][j] = 1

    result = A * B + A.transpose()*B.transpose()
    core = []
    for i in range(len(result[0])):
        for j in range(i, len(result[0])):
            if result[i, j] == 0:
                core.append([indexToName[i], indexToName[j]])

    return (core)

