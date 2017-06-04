from matplotlib import pyplot
import testerRazmerje

meseci = ["NIO_podatki_vozila_prve_reg_marec", "NIO_podatki_vozila_prve_reg_april", "NPodatki_062014", "NPodatki_072014", "NPodatki_082014", "NPodatki_092014", "NPodatki_102014", "NPodatki_112014", "NPodatki_122014", "Podatki_052014"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerRazmerje.meanStarost(mesec))

moski, zenske = 0, 0

for slovar in slovarji:
    moski += slovar['"M"']
    zenske += slovar['"Z"']


print("RAZMERJE MOSKI/ZENSKA LETA 2014 = " + str(moski/zenske))
