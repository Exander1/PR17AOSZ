from matplotlib import pyplot
import tester

meseci = ["NIO_podatki_vozila_prve_reg_marec", "NIO_podatki_vozila_prve_reg_april", "NPodatki_062014", "NPodatki_072014", "NPodatki_082014", "NPodatki_092014", "NPodatki_102014", "NPodatki_112014", "NPodatki_122014", "Podatki_052014"]
starosti = []

for mesec in meseci:
    starosti.append(tester.meanStarost(mesec))

print(sum(starosti) / len(starosti))