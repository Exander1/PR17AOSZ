from matplotlib import pyplot
import testerRazmerje

meseci = ["N2Podatki_032016", "NPodatki_012016", "NPodatki_022016", "NPodatki_042016", "NPodatki_052016", "NPodatki_062016", "NPodatki_072016", "NPodatki_082016", "NPodatki_092016", "NPodatki_102016", "NPodatki_112016", "NPodatki_122016"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerRazmerje.meanStarost(mesec))

moski, zenske = 0, 0

for slovar in slovarji:
    moski += slovar['"M"']
    zenske += slovar['"Z"']

print("RAZMERJE MOSKI/ZENSKA LETA 2016 = " + str(moski/zenske))
