from matplotlib import pyplot
import testerMoc

meseci = ["NIO_podatki_vozila_prve_reg_marec", "NIO_podatki_vozila_prve_reg_april", "NPodatki_062014", "NPodatki_072014", "NPodatki_082014", "NPodatki_092014", "NPodatki_102014", "NPodatki_112014", "NPodatki_122014", "Podatki_052014"]
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
