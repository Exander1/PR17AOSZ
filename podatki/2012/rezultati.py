from matplotlib import pyplot
import tester

meseci = ["januar2012", "februar2012", "marec2012", "april2012", "maj2012", "junij2012", "julij2012", "avgust2012", "september2012", "oktober2012", "november2012", "december2012"]
starosti = []

for mesec in meseci:
    starosti.append(tester.meanStarost(mesec))

print(sum(starosti)/len(starosti))