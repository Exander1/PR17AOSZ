import numpy as np

def meanStarost(name):
    prostornine = []
    fl = name + ".csv"
    nad4 = 0
    with open(fl, encoding="ANSI") as f:
        for row in f:
            row1 = row.split(";")
            prostornina = 0
            try:
                prostornina = float(row1[46].replace("\"", ""))
                if prostornina > 48:
                    prostornina = prostornina / 1000
                if prostornina > 4:
                    nad4 += 1
                prostornine.append(prostornina)
            except:
                pass

    return np.mean(prostornine), nad4
