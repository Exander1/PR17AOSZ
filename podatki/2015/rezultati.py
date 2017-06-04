from matplotlib import pyplot
import tester

meseci = ["NPodatki_012015", "NPodatki_022015", "NPodatki_032015", "NPodatki_042015", "NPodatki_052015", "NPodatki_062015", "NPodatki_072015", "NPodatki_082015", "NPodatki_092015", "NPodatki_102015", "NPodatki_112015", "NPodatki_122015"]
starosti = []

for mesec in meseci:
    starosti.append(tester.meanStarost(mesec))

print(sum(starosti) / len(starosti))