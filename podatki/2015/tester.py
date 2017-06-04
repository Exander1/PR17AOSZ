import numpy as np

def meanStarost(name):
    starosti = []
    fl = name + ".csv"
    with open(fl, encoding="latin-1") as f:
        for row in f:
            row1 = row.split(";")
            starost = 0
            try:
                starost = int(row1[17].replace("\"", ""))
            except:
                pass

            if starost > 0 and starost < 110:
                starosti.append(starost)

    return sum(starosti) / len(starosti)