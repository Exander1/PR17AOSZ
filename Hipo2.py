from os import getcwd  # getcwd ti pove trnenutni delavni direktorij
from glob import glob  # glob najde datoteke z podanim vzorcem
from matplotlib import pyplot as plt  # pyplot uporabimo za risanje grafov

def stRegVLetu(leto):  # stRegVLetu -> stevilo registracij v letu
    stReg = []  # v ta seznam dodajamo stevilo novih registracij po mesecih
    meseci = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    directory = getcwd() + "\podatki\\" + str(leto) + "\*.csv"  # ustvarimo primeren vzorec za uporabo v funkciji glob.
                                                                # to je trenutni delavni direktorij +
                                                                # + \podatki\ + v string spremenjeno podano leto +
                                                                # + \*.csv   Zaradi tega zadnjega isce le .csv datoteke
    for fl in glob(directory):  # glob(dir) vrne seznam datotek ki ustrezajo vzorcu dir
        with open(fl, encoding="latin-1") as f:  # vsako datoteko najdeno z glob odpremo z uporabo latin-1 encodinga
                                                 # brez tega dobimo error za nepoznane znake
            for i, l in enumerate(f):  # enumerate naredi terke z indexom vrstice in vrstico
                pass
        stReg.append(i)  # v seznam dodamo i, ki predstavlja zadnji index vrstice in enači številu registracij
                         # ne potrebujemo i+1 ker je prva vrstica, vrstica z definicijami stolpcev

    plt.plot(meseci, stReg)
    plt.xlabel("Mesec")
    plt.ylabel("stevilo registracij")
    plt.title(str(leto))
    plt.show()
    return sum(stReg)  # mesece seštejemo in vrnemo, kar predstavlja število registracij skozi celo leto.

leta = [2012, 2013, 2014, 2015, 2016]  # leta z katerimi delamo. uporabim za prikaz grafa IN računanje podatkov
stevila = []  # prazn seznam kamor se shranjuje število registracij po letu. Leta isto kot v leta seznamu
for leto in leta:
    stevila.append(stRegVLetu(leto))  # tukaj klicemo funkcijo, ki racuna stevilo registracij in si jih zapomnimo
print(stevila)

plt.plot(leta, stevila)  # še izris grafa
plt.xlabel("Leta")
plt.ylabel("Stevilo registracij")
#ax = plt.gca()
#ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()
