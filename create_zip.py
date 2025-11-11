import zipfile

files = {

    "file1.txt": "Australia#@#EV sales#@#BEV#@#2012#@#percent#@#0.5\nUSA#@#EV sales#@#BEV#@#2014#@#Vehicles#@#1200\nGermany#@#EV sales#@#PHEV#@#2016#@#Vehicles#@#500",
    "file2.txt": "USA#@#EV stock share#@#EV#@#2015#@#percent#@#0.8\nGermany#@#EV sales#@#PHEV#@#2016#@#Vehicles#@#500\nFrance#@#EV sales#@#BEV#@#2017#@#percent#@#0.7",
    "file3.txt": "UK#@#EV sales#@#BEV#@#2018#@#Vehicles#@#600\nUK#@#EV stock share#@#PHEV#@#2019#@#percent#@#1.5\nItaly#@#EV sales#@#BEV#@#2020#@#percent#@#0.3",
    "file4.txt": "Spain#@#EV sales#@#PHEV#@#2021#@#Vehicles#@#400\nSpain#@#EV stock share#@#EV#@#2022#@#percent#@#0.6\nCanada#@#EV sales#@#BEV#@#2023#@#Vehicles#@#800",
    "file5.txt": "Canada#@#EV stock share#@#PHEV#@#2010#@#percent#@#0.9\nMexico#@#EV sales#@#BEV#@#2011#@#percent#@#0.4\nBrazil#@#EV sales#@#PHEV#@#2012#@#Vehicles#@#300",
    "file6.txt": "Brazil#@#EV stock share#@#EV#@#2013#@#percent#@#1.1\nArgentina#@#EV sales#@#BEV#@#2014#@#Vehicles#@#250\nChile#@#EV sales#@#PHEV#@#2015#@#percent#@#0.6",
    "file7.txt": "Japan#@#EV sales#@#BEV#@#2016#@#Vehicles#@#700\nJapan#@#EV stock share#@#EV#@#2017#@#percent#@#0.5\nSouth Korea#@#EV sales#@#PHEV#@#2018#@#percent#@#0.8",
    "file8.txt": "India#@#EV stock share#@#EV#@#2022#@#percent#@#0.4\nRussia#@#EV sales#@#BEV#@#2023#@#Vehicles#@#350\nRussia#@#EV sales#@#PHEV#@#2024#@#percent#@#0.7",
    "file9.txt": "China#@#EV sales#@#BEV#@#2019#@#Vehicles#@#1500\nChina#@#EV stock share#@#PHEV#@#2020#@#percent#@#1.3\nIndia#@#EV sales#@#BEV#@#2021#@#percent#@#0.2",
    "file10.txt": "Norway#@#EV sales#@#BEV#@#2010#@#percent#@#0.9\nNorway#@#EV stock share#@#PHEV#@#2011#@#percent#@#1.0\nSweden#@#EV sales#@#BEV#@#2012#@#Vehicles#@#400"
}

with zipfile.ZipFile("cars.zip", "w") as z:
    for name, content in files.items():
        z.writestr(name, content)

print("cars.zip has been maded")
