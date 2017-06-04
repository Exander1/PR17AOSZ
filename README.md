# Analiza registriranih vozil med 2012 in 2016

## Alen Oberstar, Simon Zajc

## 7.5.2017


### Uvod
Cilj naloge je bilo raziskovati in odgovoriti na zastavljene hipoteze. 


### Podatki

  Namensko sva iskala problem, z veliko količino podatkov, ker sva želela preiskovati spremembe trendov skozi čas. Poleg zgoraj navedenih glavnih vprašanj, misliva, da bova lahko že razvite iskalne algoritme uporabila še na drugih potencialnih vprašanjih, ki se bodo pojavila tekom raziskovanja. Upava, da bi lahko s preiskovanjem tekočih trendov napovedala trende v avtomobilski industriji za prihajajoča leta. Zanimala bi naju tudi korelacija med nesrečami in različnimi vozniki/močmi/starostjo, a zaenkrat še nisva našla podatkov o nesrečah v Sloveniji s potrebnimi podatki.
  
Podatki so bili v zelo slabi obliki, saj so se posamezni vnosi po mesecih razlikovali in sva najprej morala prečistiti podatke, kjer sva upoštevala samo vrstice, ki so zadostovale pogojem. Stolpci se razlikujejo celo med posameznimi vnosi v istem mesecu, kar pomeni, da ima  en vnos 30 podatkov in naslednji 38, ker toliko podatkov sploh ni vnešenih za tisti mesec, namesto, da bi za določen podatek bil vnos 0, tega podatka sploh ni.

### Hipoteze

#### Hipoteza 1: Ker se povprečna starost državljanov Republike Slovenije viša, se tudi povprečna starost voznika povečuje.
#### Hipoteza 2: V zadnjih petih letih se je povečalo število prvih registracij v Sloveniji.
#### Hipoteza 3: Razmerje moški/ženska med lastniki vozil se izenačuje.
#### Hipoteza 4: Nazivne moči motorjev se s časom zmanšujejo. 
#### Hipoteza 5: Moški imajo v povprečju močnejše avtomobile. 
#### Hipoteza 6: Obstajajo obdobja v letu, v katerih je več kupljenih vozil in posledično več prvih registracij vozil. 

### Metode

Na vprašanja sva odgovarjala s pomočjo grafov, ki sva jih pridobila iz podatkov. Podatke sva uvozila v Pyhton program, ki sva ga izdelala v Pyhton 3.x s pomočjo zbirke knjižnic Anaconda. Specifično sva uporabila MatPlotLib za risanje grafov in Glob za iskanje vseh datotek v poddirektorijih nekega direktorija, ki ustrezajo določenemu vzorcu. CSV datoteke sva razdelila po letih. 


```directory = getcwd() + "\podatki\\" + str(leto) + "\*.csv"
  for fl in glob(directory): 
      with open(fl, encoding="latin-1") as f:
         for i, l in enumerate(f)
             pass
      stReg.append(i) 

```
Podatki so v 60 CSV datotekah, katere se med seboj razlikujejo, zato sva morala podatke urediti in pripraviti na obdelavo. Problem je nastal, ker niti vrstice v posamezni datoteki niso bile zapisane v istem formatu. Imele so različno število stolpcev, pa tudi, če je bilo število stolpcev enako, so bili lahko vključeni različni stolpci(Bravo slovenski statistični urad). Zaradi tega sva morala razviti svojo programsko rešitev. Program najprej ugotovi kakšno je najpogostejše število stolpcev v vrstici. Nato ročno vneseva mesto na katerem je željen podatek ter tip levega in desnega podatka, ki sta v sosednjih stolpcih željenega podatka. Program preveri če je željeni podatek pravega tipa, ter če sta levi in desni stolpec pravega tipa ali prazna. Če vrstica ustreza vsem zadanim pogojem, shranimo njen indeks in jo nato uporabimo za obdelavo. Kljub temu, da obstaja možnost napake, misliva, da zaradi količine podatkov bistveno ne vpliva na končne rezultate. Zaradi potrebe po manualnemu vnosu je z obdelavo podatkov zelo veliko dela. Če bi bili dani podatki lepo urejeni, bi bilo neizmerno lažje in hitreje iskati znanje v podatkih. 

### Rezultati
#### Hipoteza 1: Ker se povprečna starost državljanov Republike Slovenije viša, se tudi povprečna starost voznika povečuje.


#### Hipoteza 2: V zadnjih petih letih se je povečalo število prvih registracij v Sloveniji.
Kot je razvidno iz grafa 6(glej priponke) sva to hipotezo potrdila. To hipotezo sva postavila, ker je bila Slovenija leta 2012(Prvo analizirano leto) sredi ekonomske krize. Iz grafa je lepo razvidno, da se je leta 2014, ko se je stanje začelo izboljševati, prodaja avtomobilov močno povečala. Iz leta 2014 na leto 2016 je narastla za približno 30%.

#### Hipoteza 6: Obstajajo obdobja v letu, v katerih je več kupljenih vozil in posledično več prvih registracij vozil. 
Pričakovala sva, da bosta december in januar zaradi trinajste plače najbolj popularna meseca za kupovanje novih vozil. Kljub temu, da so nekateri meseci izrazito popularnejši za kupovanje vozil, se trend iz leta v leto spreminja. Zaradi relativno kratkega obdobja podatkov(5 let), iz izbranih podatkov ne moreva ugotoviti razloga za popularnejša obdobja. Zanimivo bi bilo videti(ob dosegljivosti podatkov), če imajo na to vpliv kakšne reklamne kampanje. 

### Priponke
#### Hipoteza 1
![alt text](https://cloud.githubusercontent.com/assets/13321172/26764135/2a0f106e-4961-11e7-8dba-814543729709.png)

Graf1 spreminjanja povprečne starosti državljanov Republike Slovenije

#### Hipoteza 2
Grafi registracij po mesecih v letih od 2012 do 2016:
![alt text](https://cloud.githubusercontent.com/assets/13321172/25780926/4e24dc90-3331-11e7-9c1f-df6fdb7c08b9.jpeg)

Graf 2.1: Registracije po mesecih v letu 2012.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780930/4e335eaa-3331-11e7-8b16-fc10f5269604.jpeg)

Graf 2.2: Registracije po mesecih v letu 2013.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780927/4e28c0b2-3331-11e7-89ba-ec226531b130.jpeg)

Graf 2.3: Registracije po mesecih v letu 2014.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780928/4e2bdff4-3331-11e7-8c03-206dea191d8c.jpeg)

Graf 2.4: Registracije po mesecih v letu 2015.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780929/4e2f9a90-3331-11e7-96b8-6b78d23571a9.jpeg)

Graf 2.5: Registracije po mesecih v letu 2016.

#### Hipoteza 3
![alt text](https://cloud.githubusercontent.com/assets/13321172/26764131/2a06c6b6-4961-11e7-878c-7d19f617d315.png)

Graf 3.1: Razmerje moški/ženska med lastniki vozil

#### Hipoteza 4
![alt text](https://cloud.githubusercontent.com/assets/13321172/26764133/2a0bbe5a-4961-11e7-90b6-fa68acc9841d.png)

Graf 4.1: Nazivne moči motorjev se s časom povečujejo

![alt text](https://cloud.githubusercontent.com/assets/13321172/26764134/2a0c7246-4961-11e7-9e9c-b5c4230a1573.png)

Graf 4.2: Število tovornih vozil( nad 4 litre)

#### Hipoteza 5
![alt text](https://cloud.githubusercontent.com/assets/13321172/26764132/2a0a03a8-4961-11e7-8c59-1e021890ff49.png)

Graf 5.1: Moški imajo v povprečju močnejše avtomobile

#### Hipoteza 6
![alt text](https://cloud.githubusercontent.com/assets/13321172/25780931/4e36ad6c-3331-11e7-8a0c-829d08f55f56.jpeg)

Graf 6.1
Število vseh registracij med 2012 in 2016. 


  

