import numpy as np
from collections import defaultdict

def meanStarost(name):
    slovar = defaultdict(int)
    fl = name + ".csv"
    with open(fl, encoding="ANSI") as f:
        for row in f:
            row1 = row.split(";")
            if len(row1) > 42:
                slovar[row1[42]] += 1

    return slovar
