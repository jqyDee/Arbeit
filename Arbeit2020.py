from fpdf import FPDF
import time
import os
from pathlib import Path
AktuellesDatumOhnePunkte = (time.strftime("%d%m%y"))
AktuellesDatumMitPunkte = (time.strftime("%d.%m.%y"))
AktuellesJahr = (time.strftime("%Y"))


##        Import + Time

##         Kürzel.txt File Erstellung
YN = str(input('Wenn sie nicht das heutige Datum verwenden wollen geben sie "n" ein!\n'
                'Sonst einfach "Enter" drücken!'
                ' = '))

if YN == "N":
    AktuellesDatumMitPunkte = str(input("Datum [Format: dd.mm.yy] : "))
    AktuellesDatumOhnePunkte = AktuellesDatumMitPunkte.replace(".", "")
elif YN == "n":
    AktuellesDatumMitPunkte = str(input("Datum [Format: dd.mm.yy] : "))
    AktuellesDatumOhnePunkte = AktuellesDatumMitPunkte.replace(".", "")

os.system("cls")

print("\n\n\nVerwendetes Datum: "+AktuellesDatumMitPunkte+"\n"
        "                   "+AktuellesDatumOhnePunkte+"\n\n\n")



Kürzel = str(input("Geben sie das Kürzel der Person ein!\nFormat = [2Buchstaben Nachname + 2Buchstaben Vorname]; Alles ohne Leerzeichen!; Alles Gross geschrieben\n\n\n\n        "))
os.system("cls")
print("\n\nKürzel    =    "+Kürzel+"\n\n")
Rechnungsnummer = Kürzel+AktuellesDatumOhnePunkte

os.path.isfile("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt")
my_file = Path("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt")
if my_file.exists():
    Stammdatei = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r")
    Stammdatei = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r").readlines()
else:
    Stammdatei = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "w")
    Stammdatei = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "r").readlines()


line3 = len(Stammdatei)


if line3 == 0:
    Stammdatei = open("E:\\Mervi\\Rechnungen\\Stammdaten\\"+Kürzel+".txt", "w")
    Kürzel = Kürzel
    Rechnungsnummer = (Kürzel+AktuellesDatumOhnePunkte)
    c = AktuellesDatumMitPunkte
    Stammdatei.write(Kürzel+"\n")
    f = str(input("Mann/Frau: "))
    Stammdatei.write(""+f+"\n")
    e = str(input("Nachname: "))
    Stammdatei.write(""+e+"\n")
    d = str(input("Vorname: "))
    Stammdatei.write(""+d+"\n")
    g = str(input("Strasse: "))
    Stammdatei.write(""+g+"\n")
    j = str(input("Hausnummer: "))
    Stammdatei.write(""+j+"\n")
    i = str(input("PLZ: "))
    Stammdatei.write(""+i+"\n")
    h = str(input("Ort: "))
    Stammdatei.write(""+h+"\n")
    Stammdatei.write(input("Geburtsdatum: ")+"\n")
    k = int(input("Strecke zu fahren: "))
    Stammdatei.write(""+str(k)+"\n")
    Stammdatei.write(input("Hausarzt: ")+"\n")
    Stammdatei.close()


else:
    print(Kürzel+" existiert bereits!")
    lines = Stammdatei
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')

    Kürzel = lines[0]
    Rechnungsnummer = (Kürzel+AktuellesDatumOhnePunkte)
    c = AktuellesDatumMitPunkte
    d = lines[3]
    e = lines[2]
    f = lines[1]
    g = lines[4]
    h = lines[7]
    i = lines[6]
    j = lines[5]
    k = lines[9]

    k = int(k)


pdf = FPDF()
#Header 1
pdf.add_page()
pdf.set_font("Arial", "B""U", 25)
pdf.set_text_color(255, 0, 0)
pdf.set_draw_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 10, "Rechnung", border=1, ln=1, align="C")

#Header 2
pdf.set_font("Arial", "B", 15)
pdf.set_text_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 7, "Mervi Fischbach", ln=1, align="C")

#Header 3
pdf.set_font("Arial", "B", 15)
pdf.set_text_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 7, "Physiotherapeutin", ln=1, align="C")

#Header 3
pdf.set_font("Arial", "B", 13)
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 3.5, "", ln=1, align="C")
pdf.cell(1)
pdf.cell(0, 6, "Schulgasse 9    86923 Finning", ln=1, align="C")

#Abschnitt 1

pdf.set_font("Arial", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 4, "", ln=1, align="C")
if f == "Mann":
    pdf.write(6.5, "Herr "+d+" "+e)
elif f == "Frau":
    pdf.write(6.5, "Frau "+d+" "+e)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.write(6.5, ""+g+" "+j)
pdf.cell(0, 10, "", ln=1, align="C")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, ""+i+" "+h)

#Abschnitt 2
pdf.set_font("Arial", "B", 13)
pdf.set_text_color(0,0,0)
pdf.cell(0, 15, "", ln=1, align="C")
pdf.write(6.5, "Patient"+"                                              "+"Rechnungsnummer"+"                                        "+"Datum")
pdf.set_font("Arial", "", 13)
pdf.cell(0, 6, "", ln=1, align="C")
pdf.write(6.5, ""+Kürzel+"                                                     "+Rechnungsnummer+"                                            "+c)

#Abschnitt 3
o = int(input("Anzahl der Behandlungstermine: "))
u1 = str(input("Behandlungsdatum 1 (dd.mm.jj): ")); u2 = str(input("Behandlungsdatum 2 (dd.mm.jj): ")); u3 = str(input("Behandlungsdatum 3 (dd.mm.jj): ")); u4 = str(input("Behandlungsdatum 4 (dd.mm.jj): ")); u5 = str(input("Behandlungsdatum 5 (dd.mm.jj): ")); u6 = str(input("Behandlungsdatum 6 (dd.mm.jj): ")); u7 = str(input("Behandlungsdatum 7 (dd.mm.jj): ")); u8 = str(input("Behandlungsdatum 8 (dd.mm.jj): ")); u9 = str(input("Behandlungsdatum 9 (dd.mm.jj): ")); u10 = str(input("Behandlungsdatum 10 (dd.mm.jj): "))
pdf.cell(0, 15, "", ln=1, align="C")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, ""+str(o)+" Behandlungstermine:\n")
pdf.set_font("Arial", "", 12)
pdf.write(6.5, ""+u1+"             "+u2+" \n")
pdf.write(6.5, ""+u3+"             "+u4+" \n")
pdf.write(6.5, ""+u5+"             "+u6+" \n")
pdf.write(6.5, ""+u7+"             "+u8+" \n")
pdf.write(6.5, ""+u9+"             "+u10+"\n")


#Abschnitt 4
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "", ln=1, align="C")
if f == "Mann":
    pdf.write(6.5, "Sehr geehrter Herr "+e+",\n")
    pdf.write(8, "hiermit erlaube ich mir, für meine Bemühungen folgendes Honorar zu berechnen:")
elif f == "Frau":
    pdf.write(6.5, "Sehr geehrte Frau "+e+",\n")
    pdf.write(8, "hiermit erlaube ich mir, für meine Bemühungen folgendes Honorar zu berechnen:")

#Abschnitt 5
pdf.set_font("Arial", "", 12)
pdf.cell(0, 12, "", ln=1, align="C")
pdf.write(6.5, "1      Anamnese + Befunderhebung;          ")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, "Einzelpreis: 00,00 Euro\n")

intt = int(input("Anzahl der Arten der Behandlung (Nur Zahlen von 1 bis 5!): "))
zero = 0
plpl = 0
while zero < intt:
    zero += 1
    kl = str(input("Behandlungsart: "))
    l = float(input("Einzelpreis (Format: 00.00)(Kein Komma sondern ein Punkt!): "))
    positionl = str(l).find(".")
    positionl = positionl + 1
    lcheck = str(l)[positionl:]
    lenlcheck = len(str(lcheck))

    if lenlcheck == 1:
        l = str(l)+"0"

    l = str(l).replace(".", ",")
    pdf.set_font("Arial", "", 12)
    pdf.write(6.5, ""+str(o)+"      "+str(kl)+";          ")
    pdf.set_font("Arial", "B", 12)
    pdf.write(6.5, "Einzelpreis: "+str(l)+" Euro\n")
    l = str(l).replace(",", ".")

    plpl += o*float(l)


#Abschnitt 6
plpl = str(plpl)
lenplpl = len(plpl)
position = plpl.find(".")
position = position + 1
Ausgabe = lenplpl - position
if Ausgabe == 1:
    plpl = str(plpl)+"0"
    plpl = plpl.replace(".", ",")

pdf.set_font("Arial", "", 12)
pdf.cell(0, 6, "", ln=1, align="C")
pdf.write(6.5, "Ich bitte Sie, den Gesamtbetrag von "+str(plpl)+" Euro innerhalb von 14 Tagen unter Angabe der Rechnungsnummer auf unten stehendes Konto zu überweisen.")
pdf.cell(0, 13, "", ln=1, align="C")
pdf.set_font("Arial", "", 13)
pdf.write(6.5, "Mit freundlichen Grüßen")
pdf.cell(0, 20, "", ln=1, align="C")
pdf.write(6.5, "Mervi Fischbach")

#Abschnitt 7
pdf.set_font("Arial", "B", 10)
pdf.set_text_color(0, 0, 0)
pdf.set_draw_color(0, 0, 0)
pdf.cell(0, 10, "", ln=1, align="C")
pdf.cell(1)
pdf.cell(0, 3, "Bankverbindung", ln=1, align="C")
pdf.cell(0, 3, "ING Diba", ln=1, align="C")
pdf.cell(0, 3, "IBAN - DE 20 500 105 17 540 350 6861", ln=1, align="C")
pdf.cell(0, 3, "BIC - INGDDEFFXXX", ln=1, align="C")
pdf.set_font("Arial", "B", 8)
pdf.cell(0, 3, "Steuer Nummer: 131-217-00314", ln=1, align="C")

#Lines
pdf.set_draw_color(0,0,0)
pdf.line(10,93,200,93)
pdf.line(10,73,200,73)
pdf.line(10,143,200,143)


#Infos
#PDF Speichern
pdf.ln(100)
pdf.output("E:\\Mervi\\Rechnungen\\Rechnungen\\Rechnungen2020\\"+Rechnungsnummer+".pdf")


#______________________________________________________________________________________________________
#Speichern der Daten in die TXT Datei

m = 2*k*o
os.path.isfile("E:\\Mervi\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2020.txt")
my_file = Path("E:\\Mervi\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2020.txt")
if my_file.exists():
    DateiMitKurzel = open("E:\\Mervi\\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2020.txt", "a")
    DateiMitKurzel.write("\n"+str(Kürzel)+";"+str(Rechnungsnummer)+";"+str(k)+";km;"+str(m)+";km;"+str(plpl)+";Euro;"+u1+";"+u2+";"+u3+";"+u4+";"+u5+";"+u6+";"+u7+";"+u8+";"+u9+";"+u10+";")
else:
    DateiMitKurzel = open("E:\\Mervi\\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2020.txt", "w")
    DateiMitKurzel.write("\n"+str(Kürzel)+";"+str(Rechnungsnummer)+";"+str(k)+";km;"+str(m)+";km;"+str(plpl)+";Euro;"+u1+";"+u2+";"+u3+";"+u4+";"+u5+";"+u6+";"+u7+";"+u8+";"+u9+";"+u10+";")
