from matplotlib import pyplot
import testerRazmerje

meseci = ["januar2013", "februar2013", "marec2013", "april2013", "maj2013", "junij2013", "julij2013", "avgust2013", "september2013", "oktober2013", "november2013", "december2013"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerRazmerje.meanStarost(mesec))

moski, zenske = 0, 0

for slovar in slovarji:
    moski += slovar['"M"']
    zenske += slovar['"Ž"']

print("RAZMERJE MOSKI/ZENSKA LETA 2013 = " + str(moski/zenske))
