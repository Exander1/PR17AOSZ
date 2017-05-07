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



### Rezultati
Grafi registracij po mesecih v letih od 2012 do 2016.
![alt text](https://cloud.githubusercontent.com/assets/13321172/25780926/4e24dc90-3331-11e7-9c1f-df6fdb7c08b9.jpeg)

Graf 1: Registracije po mesecih v letu 2012.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780930/4e335eaa-3331-11e7-8b16-fc10f5269604.jpeg)

Graf 2: Registracije po mesecih v letu 2013.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780927/4e28c0b2-3331-11e7-89ba-ec226531b130.jpeg)

Graf 3: Registracije po mesecih v letu 2014.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780928/4e2bdff4-3331-11e7-8c03-206dea191d8c.jpeg)

Graf 4: Registracije po mesecih v letu 2015.

![alt text](https://cloud.githubusercontent.com/assets/13321172/25780929/4e2f9a90-3331-11e7-96b8-6b78d23571a9.jpeg)

Graf 5: Registracije po mesecih v letu 2016.


![alt text](https://cloud.githubusercontent.com/assets/13321172/25780931/4e36ad6c-3331-11e7-8a0c-829d08f55f56.jpeg)

Graf 6: Število vseh registracij med 2012 in 2016.  


  

