from matplotlib import pyplot
import tester

meseci = ["N2Podatki_032016", "NPodatki_012016", "NPodatki_022016", "NPodatki_042016", "NPodatki_052016", "NPodatki_062016", "NPodatki_072016", "NPodatki_082016", "NPodatki_092016", "NPodatki_102016", "NPodatki_112016", "NPodatki_122016"]
starosti = []

for mesec in meseci:
    starosti.append(tester.meanStarost(mesec))

print(sum(starosti) / len(starosti))