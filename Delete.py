import fileinput
import os

phrase = input("Welche Datei soll gelöscht werden (Rechnungsnummer eingeben): ")
for line in fileinput.input("E:\\Mervi\\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2020.txt", inplace=True):
    if phrase in line:
        continue
    print(line, end='')

if os.path.exists("E:\\Mervi\\Rechnungen\\Rechnungen\\Rechnungen2020\\"+phrase+".pdf"):
    os.remove("E:\\Mervi\\Rechnungen\\Rechnungen\\Rechnungen2020\\"+phrase+".pdf")
else:
  print("The file does not exist ("+phrase+".pdf)") 
