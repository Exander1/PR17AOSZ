from matplotlib import pyplot
import tester

meseci = ["januar2013", "februar2013", "marec2013", "april2013", "maj2013", "junij2013", "julij2013", "avgust2013", "september2013", "oktober2013", "november2013", "december2013"]
starosti = []

for mesec in meseci:
    starosti.append(tester.meanStarost(mesec))

print(sum(starosti) /+ len(starosti))