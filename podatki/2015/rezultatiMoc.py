from matplotlib import pyplot
import testerMoc

meseci = ["NPodatki_012015", "NPodatki_022015", "NPodatki_032015", "NPodatki_042015", "NPodatki_052015", "NPodatki_062015", "NPodatki_072015", "NPodatki_082015", "NPodatki_092015", "NPodatki_102015", "NPodatki_112015", "NPodatki_122015"]
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
