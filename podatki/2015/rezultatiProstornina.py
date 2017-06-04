from matplotlib import pyplot
import testerProstornina

meseci = ["NPodatki_012015", "NPodatki_022015", "NPodatki_032015", "NPodatki_042015", "NPodatki_052015", "NPodatki_062015", "NPodatki_072015", "NPodatki_082015", "NPodatki_092015", "NPodatki_102015", "NPodatki_112015", "NPodatki_122015"]
prostornine = []
nad4 = []

for mesec in meseci:
    nekej = testerProstornina.meanStarost(mesec)
    prostornine.append(nekej[0])
    nad4.append(nekej[1])

print(sum(prostornine)/len(prostornine))
print(sum(nad4))