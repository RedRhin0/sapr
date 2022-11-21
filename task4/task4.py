from io import StringIO
import csv
import math


def getNodeList(graph):
    nodeMap = {}
    for [par, ch] in graph:
        nodeMap[par] = True
        nodeMap[ch] = True
    return list(nodeMap.keys())


def getChilds(node, graph):
    childs = []
    for [par, ch] in graph:
        if par == node:
            childs.append(ch)
    return childs


def getParents(node, graph):
    parents = []
    for [par, ch] in graph:
        if ch == node:
            parents.append(par)
    return parents


def getAncestors(node, graph):
    ancestors = []
    parents = getParents(node, graph)
    for par in parents:
        grandParents = getParents(par, graph)
        if len(grandParents) > 0:
            ancestors.extend(grandParents)
            ancestors.extend(getAncestors(par, graph))
    return ancestors


def getDescendants(node, graph):
    descendants = []
    children = getChilds(node, graph)
    for child in children:
        grandChildren = getChilds(child, graph)
        if len(grandChildren) > 0:
            descendants.extend(grandChildren)
            descendants.extend(getAncestors(child, graph))
    return descendants


def getNeighbours(node, graph):
    parents = getParents(node, graph)
    neighbours = []
    for parent in parents:
        children = getChilds(parent, graph)
        children.remove(node)
        neighbours.extend(children)
    return neighbours


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    nodeList = getNodeList(graph)
    graphStats = []
    for node in nodeList:
        graphStats.append([node, [len(getChilds(node, graph)), len(getParents(node, graph)), len(
            getDescendants(node, graph)), len(getAncestors(node, graph)), len(getNeighbours(node, graph))]])

    entropy = 0
    n = len(graphStats)
    for [node, nodeStats] in graphStats:
        in_sum = 0
        for i in nodeStats:
            p = i/(n-1)
            if p > 0:
                in_sum += p*math.log(p, 2)
        entropy += in_sum

    return -entropy