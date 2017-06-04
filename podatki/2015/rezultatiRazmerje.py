from matplotlib import pyplot
import testerRazmerje

meseci = ["NPodatki_012015", "NPodatki_022015", "NPodatki_032015", "NPodatki_042015", "NPodatki_052015", "NPodatki_062015", "NPodatki_072015", "NPodatki_082015", "NPodatki_092015", "NPodatki_102015", "NPodatki_112015", "NPodatki_122015"]
slovarji = []

for mesec in meseci:
    slovarji.append(testerRazmerje.meanStarost(mesec))

moski, zenske = 0, 0

for slovar in slovarji:
    moski += slovar['"M"']
    zenske += slovar['"Z"']

print("RAZMERJE MOSKI/ZENSKA LETA 2015 = " + str(moski/zenske))
