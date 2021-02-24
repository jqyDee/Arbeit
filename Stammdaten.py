from fpdf import FPDF
import time
import os
from pathlib import Path
AktuellesDatum = (time.strftime("%d%m%y"))
AktuellesDatum2 = (time.strftime("%d.%m.%Y"))
AktuellesJahr = (time.strftime("%Y"))


##        Import + Time

##         Kürzel.txt File Erstellung



Kürzel = str(input("Geben sie das Kürzel der Person ein!\n"
                   "Format = [2Buchstaben Nachname + 2Buchstaben Vorname]; Alles ohne Leerzeichen!; Alles Groß geschrieben\n"
                   "\n"
                   "=   "))

DateiMitKürzelMitDatum = Kürzel+AktuellesDatum

os.path.isfile("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt")
my_file = Path("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt")
if my_file.exists():
    DateiMitKürzel = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r")
    DateiMitKürzel = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r").readlines()
else:
    DateiMitKürzel = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "w")
    DateiMitKürzel = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r").readlines()


line3 = len(DateiMitKürzel)


if line3 == 0:
    DateiMitKürzel = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "w")
    a = Kürzel
    b = (a+AktuellesDatum)
    c = AktuellesDatum2
    DateiMitKürzel.write(a+"\n")
    f = str(input("Mann/Frau: "))
    DateiMitKürzel.write(""+f+"\n")
    e = str(input("Nachname: "))
    DateiMitKürzel.write(""+e+"\n")
    d = str(input("Vorname: "))
    DateiMitKürzel.write(""+d+"\n")
    g = str(input("Strasse: "))
    DateiMitKürzel.write(""+g+"\n")
    j = str(input("Hausnummer: "))
    DateiMitKürzel.write(""+j+"\n")
    i = str(input("PLZ: "))
    DateiMitKürzel.write(""+i+"\n")
    h = str(input("Ort: "))
    DateiMitKürzel.write(""+h+"\n")
    DateiMitKürzel.write(input("Geburtsdatum: ")+"\n")
    k = int(input("Strecke zu fahren: "))
    DateiMitKürzel.write(""+str(k)+"\n")
    DateiMitKürzel.write(input("Hausarzt: ")+"\n")
    DateiMitKürzel.close()


else:
    print(Kürzel+" existiert bereits!")
