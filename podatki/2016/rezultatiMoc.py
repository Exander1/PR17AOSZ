from matplotlib import pyplot
import testerMoc

meseci = ["N2Podatki_032016", "NPodatki_012016", "NPodatki_022016", "NPodatki_042016", "NPodatki_052016", "NPodatki_062016", "NPodatki_072016", "NPodatki_082016", "NPodatki_092016", "NPodatki_102016", "NPodatki_112016", "NPodatki_122016"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerMoc.meanStarost(mesec))

moski, zenske, moskiMoc, zenskeMoc = 0, 0, 0, 0

for slovar in slovarji:
    moski += slovar['M']
    #print(moski)
    zenske += slovar['Z']
    #print(zenske)
    moskiMoc += slovar['MMoc']
    zenskeMoc += slovar['ZMoc']


print("Povprecni moski ima avto mocan: " + str(moskiMoc/moski) + " KW")
print("Povprecna zenska ima avto mocan: " + str(zenskeMoc/zenske) + " KW")
