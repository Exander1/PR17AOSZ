import numpy as np

def meanStarost(name):
    starosti = []
    nekej = 0
    fl = name + ".csv"
    with open(fl, encoding="latin-1") as f:
        for row in f:
            row1 = row.split(";")
            starost = 0
            try:
                starost = int(row1[40])
            except:
                print("line : " + str(nekej) + " : " + row1[40])
                pass

            if starost > 0 and starost < 110:
                starosti.append(starost)
            nekej += 1

    return np.mean(starosti)

meanStarost("januar2012")