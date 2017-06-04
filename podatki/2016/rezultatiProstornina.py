from matplotlib import pyplot
import testerProstornina

meseci = ["N2Podatki_032016", "NPodatki_012016", "NPodatki_022016", "NPodatki_042016", "NPodatki_052016", "NPodatki_062016", "NPodatki_072016", "NPodatki_082016", "NPodatki_092016", "NPodatki_102016", "NPodatki_112016", "NPodatki_122016"]
prostornine = []
nad4 = []

for mesec in meseci:
    nekej = testerProstornina.meanStarost(mesec)
    prostornine.append(nekej[0])
    nad4.append(nekej[1])

print(sum(prostornine)/len(prostornine))
print(sum(nad4))