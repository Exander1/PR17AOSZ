from matplotlib import pyplot
import testerProstornina

meseci = ["januar2012", "februar2012", "marec2012", "april2012", "maj2012", "junij2012", "julij2012", "avgust2012", "september2012", "oktober2012", "november2012", "december2012"]
prostornine = []
nad4 = []

for mesec in meseci:
    nekej = testerProstornina.meanStarost(mesec)
    prostornine.append(nekej[0])
    nad4.append(nekej[1])

print(sum(prostornine)/len(prostornine))
print(sum(nad4))
