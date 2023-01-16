import csv
from io import StringIO


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for line in reader:
        graph.append([int(x) for x in line])

    r1 = {}
    r2 = {}
    r3 = {}
    r4 = {}
    r5 = {}

    for [l, r] in graph:
        r1[l] = l
        r2[r] = True
        for [i, j] in graph:
            if r == i:
                r3[l] = True
                r4[j] = True
            if (l == i) & (r != j):
                r5[r] = True

    return [list(r1.keys()), list(r2.keys()), list(r3.keys()), list(r4.keys()), list(r5.keys())]