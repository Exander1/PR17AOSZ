from matplotlib import pyplot
import testerRazmerje

meseci = ["januar2012", "februar2012", "marec2012", "april2012", "maj2012", "junij2012", "julij2012", "avgust2012", "september2012", "oktober2012", "november2012", "december2012"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerRazmerje.meanStarost(mesec))

moski, zenske = 0, 0

for slovar in slovarji:
    moski += slovar['"M"']
    zenske += slovar['"Ž"']

print("RAZMERJE MOSKI/ZENSKA LETA 2012 = " + str(moski/zenske))
