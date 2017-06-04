import numpy as np
from collections import defaultdict

def meanStarost(name):
    slovar = defaultdict(int)
    fl = name + ".csv"
    with open(fl, encoding="ANSI") as f:
        for row in f:
            row1 = row.split(";")
            try:
                moc = int(row1[47].replace("\"", ""))
                if moc > 20:
                    if row1[19] == '"M"':
                        slovar['M'] += 1
                        slovar['MMoc'] += moc
                    elif row1[19] == '"Z"':
                        slovar['Z'] += 1
                        slovar['ZMoc'] += moc
            except:
                pass

    return slovar
