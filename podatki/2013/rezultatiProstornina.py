from matplotlib import pyplot
import testerProstornina

meseci = ["januar2013", "februar2013", "marec2013", "april2013", "maj2013", "junij2013", "julij2013", "avgust2013", "september2013", "oktober2013", "november2013", "december2013"]
prostornine = []
nad4 = []

for mesec in meseci:
    nekej = testerProstornina.meanStarost(mesec)
    prostornine.append(nekej[0])
    nad4.append(nekej[1])

print(sum(prostornine)/len(prostornine))
print(sum(nad4))
