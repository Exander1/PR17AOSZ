from matplotlib import pyplot
import testerProstornina

meseci = ["NIO_podatki_vozila_prve_reg_marec", "NIO_podatki_vozila_prve_reg_april", "NPodatki_062014", "NPodatki_072014", "NPodatki_082014", "NPodatki_092014", "NPodatki_102014", "NPodatki_112014", "NPodatki_122014", "Podatki_052014"]
prostornine = []
nad4 = []

for mesec in meseci:
    nekej = testerProstornina.meanStarost(mesec)
    prostornine.append(nekej[0])
    nad4.append(nekej[1])

print(sum(prostornine)/len(prostornine))
print(sum(nad4))