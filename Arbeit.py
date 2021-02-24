# Import + Time
from fpdf import FPDF
import time
import os
import sys
from pathlib import Path

AktuellesDatumOhnePunkte = (time.strftime("%d%m%y"))
AktuellesDatum = (time.strftime("%d.%m.%y"))

# Heutiges Datum , ja/nein
YN = str(input('Wenn sie nicht das heutige Datum verwenden wollen geben sie "n" ein!\n'
               'Sonst einfach "Enter" drücken!'
               ' = '))

if YN == "N":
    AktuellesDatum = str(input("Datum [Format: dd.mm.yy] : "))
    AktuellesDatumOhnePunkte = AktuellesDatum.replace(".", "")
elif YN == "n":
    AktuellesDatum = str(input("Datum [Format: dd.mm.yy] : "))
    AktuellesDatumOhnePunkte = AktuellesDatum.replace(".", "")

os.system("cls")

print("\n\n\nVerwendetes Datum: " + AktuellesDatum + "\n"
                                                     "                   " + AktuellesDatumOhnePunkte + "\n\n\n")

# Kürzel überprüfung, sowie Erstellung der Datum/Laden der Datei
Kürzel = str(input(
    "Geben sie das Kürzel der Person ein!\nFormat = [2Buchstaben Nachname + 2Buchstaben Vorname]; Alles ohne Leerzeichen!; Alles Gross geschrieben\n\n\n\n        "))
os.system("cls")
print("\n\nKürzel    =    " + Kürzel)

Rechnungsnummer = (Kürzel + AktuellesDatumOhnePunkte)
print("Rechnungsnummer    =    " + Rechnungsnummer + "\n\n")

os.path.isfile("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt")
my_file = Path("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt")
if my_file.exists():
    Stammdatei = open("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt", "r")
    Stammdatei = open("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt", "r").readlines()
else:
    Stammdatei = open("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt", "w")
    Stammdatei = open("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt", "r").readlines()

LinesInStammdatei = len(Stammdatei)

if LinesInStammdatei == 0:
    Stammdatei = open("E:\\KGRechnungsprogramm\\Rechnungen\\Stammdaten\\" + Kürzel + ".txt", "w")
    Stammdatei.write(Kürzel + "\n")
    MaFr = str(input("Mann/Frau: "))
    Stammdatei.write("" + MaFr + "\n")
    Nachname = str(input("Nachname: "))
    Stammdatei.write("" + Nachname + "\n")
    Vorname = str(input("Vorname: "))
    Stammdatei.write("" + Vorname + "\n")
    Strasse = str(input("Strasse: "))
    Stammdatei.write("" + Strasse + "\n")
    Hausnummer = str(input("Hausnummer: "))
    Stammdatei.write("" + Hausnummer + "\n")
    PLZ = str(input("PLZ: "))
    Stammdatei.write("" + PLZ + "\n")
    Ort = str(input("Ort: "))
    Stammdatei.write("" + Ort + "\n")
    Geburtsdatum = str(input("Geburtsdatum: "))
    Stammdatei.write("" + Geburtsdatum + "\n")
    KilometerZuFahren = int(input("Strecke zu fahren: "))
    Stammdatei.write("" + str(KilometerZuFahren) + "\n")
    Hausarzt = str(input("Hausarzt: "))
    Stammdatei.write(Hausarzt + "\n")
    Stammdatei.close()


else:
    print(Kürzel + " existiert bereits!")
    lines = Stammdatei
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')

    Kürzel = lines[0]
    Vorname = lines[3]
    Nachname = lines[2]
    MaFr = lines[1]
    Strasse = lines[4]
    Ort = lines[7]
    PLZ = lines[6]
    Hausnummer = lines[5]
    Geburtsdatum = lines[8]
    KilometerZuFahren = lines[9]
    Hausarzt = lines[10]

    KilometerZuFahren = int(KilometerZuFahren)

pdf = FPDF()
# Header 1
pdf.add_page()
pdf.set_font("Arial", "B""U", 25)
pdf.set_text_color(255, 0, 0)
pdf.set_draw_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 10, "Rechnung", border=1, ln=1, align="C")

# Header 2
pdf.set_font("Arial", "B", 15)
pdf.set_text_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 7, "Mervi Fischbach", ln=1, align="C")

# Header 3
pdf.set_font("Arial", "B", 15)
pdf.set_text_color(255, 0, 0)
pdf.cell(1)
pdf.cell(0, 7, "Physiotherapeutin", ln=1, align="C")

# Header 3
pdf.set_font("Arial", "B", 13)
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 3.5, "", ln=1, align="C")
pdf.cell(1)
pdf.cell(0, 6, "Schulgasse 9    86923 Finning", ln=1, align="C")

# Abschnitt 1

pdf.set_font("Arial", "", 12)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 4, "", ln=1, align="C")
if MaFr == "Mann":
    pdf.write(6.5, "Herr " + Vorname + " " + Nachname)
elif MaFr == "Frau":
    pdf.write(6.5, "Frau " + Vorname + " " + Nachname)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.write(6.5, "" + Strasse + " " + Hausnummer)
pdf.cell(0, 10, "", ln=1, align="C")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, "" + PLZ + " " + Ort)

# Abschnitt 2
pdf.set_font("Arial", "B", 13)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 15, "", ln=1, align="C")
pdf.write(6.5,
          "Patient" + "                                              " + "Rechnungsnummer" + "                                        " + "Datum")
pdf.set_font("Arial", "", 13)
pdf.cell(0, 6, "", ln=1, align="C")
pdf.write(6.5,
          "" + Kürzel + "                                                     " + Rechnungsnummer + "                                            " + AktuellesDatum)

# Abschnitt 3
os.system("cls")
intBehandlungstermine = int(input("Anzahl der Behandlungstermine: "))
u1 = str(input("Behandlungsdatum 1 (dd.mm.jj): "));
u2 = str(input("Behandlungsdatum 2 (dd.mm.jj): "));
u3 = str(input("Behandlungsdatum 3 (dd.mm.jj): "));
u4 = str(input("Behandlungsdatum 4 (dd.mm.jj): "));
u5 = str(input("Behandlungsdatum 5 (dd.mm.jj): "));
u6 = str(input("Behandlungsdatum 6 (dd.mm.jj): "));
u7 = str(input("Behandlungsdatum 7 (dd.mm.jj): "));
u8 = str(input("Behandlungsdatum 8 (dd.mm.jj): "));
u9 = str(input("Behandlungsdatum 9 (dd.mm.jj): "));
u10 = str(input("Behandlungsdatum 10 (dd.mm.jj): "))
pdf.cell(0, 15, "", ln=1, align="C")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, "" + str(intBehandlungstermine) + " Behandlungstermine:\n")
pdf.set_font("Arial", "", 12)
pdf.write(6.5, "" + u1 + "             " + u2 + " \n")
pdf.write(6.5, "" + u3 + "             " + u4 + " \n")
pdf.write(6.5, "" + u5 + "             " + u6 + " \n")
pdf.write(6.5, "" + u7 + "             " + u8 + " \n")
pdf.write(6.5, "" + u9 + "             " + u10 + "\n")

# Abschnitt 4
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "", ln=1, align="C")
if MaFr == "Mann":
    pdf.write(6.5, "Sehr geehrter Herr " + Nachname + ",\n")
    pdf.write(8, "hiermit erlaube ich mir, für meine Bemühungen folgendes Honorar zu berechnen:")
elif MaFr == "Frau":
    pdf.write(6.5, "Sehr geehrte Frau " + Nachname + ",\n")
    pdf.write(8, "hiermit erlaube ich mir, für meine Bemühungen folgendes Honorar zu berechnen:")

# Abschnitt 5
pdf.set_font("Arial", "", 12)
pdf.cell(0, 12, "", ln=1, align="C")
pdf.write(6.5, "1      Anamnese + Befunderhebung;          ")
pdf.set_font("Arial", "B", 12)
pdf.write(6.5, "Einzelpreis: 00,00 Euro\n")

intt = int(input("\n\nAnzahl der Arten der Behandlung (Nur Zahlen von 1 bis 5!): "))
zero = 0
gesamtPreis = 0
BehandlungsartenGesamt = ""
while zero < intt:
    zero += 1
    kl = str(input("Behandlungsart: "))
    l = float(input("Einzelpreis (Format: 00.00)(Kein Komma sondern ein Punkt!): "))
    positionl = str(l).find(".")
    positionl = positionl + 1
    lcheck = str(l)[positionl:]
    lenlcheck = len(str(lcheck))

    if lenlcheck == 1:
        l = str(l) + "0"

    l = str(l).replace(".", ",")
    pdf.set_font("Arial", "", 12)
    pdf.write(6.5, "" + str(intBehandlungstermine) + "      " + str(kl) + ";          ")
    pdf.set_font("Arial", "B", 12)
    pdf.write(6.5, "Einzelpreis: " + str(l) + " Euro\n")
    l = str(l).replace(",", ".")

    gesamtPreis += intBehandlungstermine * float(l)

    BehandlungsartenGesamt += "ü" + kl + ", " + l + ";"

BehandlungsartenGesamt = BehandlungsartenGesamt.replace("ü", "Behandlungsart: ")
BehandlungsartenGesamt = BehandlungsartenGesamt.replace(";", "\n")
print(BehandlungsartenGesamt)

# Abschnitt 6
gesamtPreis = str(gesamtPreis)
lenplpl = len(gesamtPreis)
position = gesamtPreis.find(".")
position = position + 1
Ausgabe = lenplpl - position
if Ausgabe == 1:
    gesamtPreis = str(gesamtPreis) + "0"
    gesamtPreis = gesamtPreis.replace(".", ",")

pdf.set_font("Arial", "", 12)
pdf.cell(0, 6, "", ln=1, align="C")
pdf.write(6.5, "Ich bitte Sie, den Gesamtbetrag von " + str(
    gesamtPreis) + " Euro innerhalb von 14 Tagen unter Angabe der Rechnungsnummer auf unten stehendes Konto zu überweisen.")
pdf.cell(0, 13, "", ln=1, align="C")
pdf.set_font("Arial", "", 13)
pdf.write(6.5, "Mit freundlichen Grüßen")
pdf.cell(0, 20, "", ln=1, align="C")
pdf.write(6.5, "Mervi Fischbach")

# Abschnitt 7
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

# Lines
pdf.set_draw_color(0, 0, 0)
pdf.line(10, 93, 200, 93)
pdf.line(10, 73, 200, 73)
pdf.line(10, 143, 200, 143)

# Infos
os.system("cls")

BehandlungsartenGesamt = BehandlungsartenGesamt.replace("ü", "Behandlungsart: ")
BehandlungsartenGesamt = BehandlungsartenGesamt.replace(";", "\n")
print("Stammdaten:\nKürzel: " + str(Kürzel) + "\nMann/Frau; " + str(MaFr) + "\nVorname: " + str(
    Vorname) + "\nNachname: " + str(Nachname) + "\nStrasse: " + str(Strasse) + "\nHausnummer: " + str(
    Hausnummer) + "\nPLZ: " + str(PLZ) + "\nOrt: " + str(Ort) + "\nGeburtsdatum: " + str(
    Geburtsdatum) + "\nKilometer zu fahren: " + str(KilometerZuFahren) + "\nHausarzt: " + str(
    Hausarzt) + "\n\nDaten:\n" + u1 + "; " + u2 + "\n" + u3 + "; " + u4 + "\n" + u5 + "; " + u6 + "\n" + u7 + "; " + u8 + "\n" + u9 + "; " + u10 + "\n\nBehandlungsarten: \n" + BehandlungsartenGesamt)

Platzhalter = 0
while Platzhalter != "n" and Platzhalter != "y":
    Platzhalter = input("Program beenden und Daten speichern? (y/n) : ")
    if Platzhalter == "y":
        # PDF Speichern
        pdf.ln(100)
        pdf.output("E:\\KGRechnungsprogramm\\Rechnungen\\Rechnungen\\Rechnungen2021\\" + Rechnungsnummer + ".pdf")

        # ______________________________________________________________________________________________________
        # Speichern der Daten in die TXT Datei
        insgKilometer = 2 * KilometerZuFahren * intBehandlungstermine
        os.path.isfile("E:\\KGRechnungsprogramm\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2021.txt")
        my_file = Path("E:\\KGRechnungsprogramm\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2021.txt")
        if my_file.exists():
            DateiMitKurzel = open(
                "E:\\KGRechnungsprogramm\\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2021.txt", "a")
            DateiMitKurzel.write(
                "\n" + str(Kürzel) + ";" + str(Rechnungsnummer) + ";" + str(KilometerZuFahren) + ";km;" + str(
                    insgKilometer) + ";km;" + str(
                    gesamtPreis) + ";Euro;" + u1 + ";" + u2 + ";" + u3 + ";" + u4 + ";" + u5 + ";" + u6 + ";" + u7 + ";" + u8 + ";" + u9 + ";" + u10 + ";")
        else:
            DateiMitKurzel = open(
                "E:\\KGRechnungsprogramm\\Rechnungen\\ZusammenfassungRechnungen\\RechnungenInsgesamt2021.txt", "w")
            DateiMitKurzel.write(
                "\n" + str(Kürzel) + ";" + str(Rechnungsnummer) + ";" + str(KilometerZuFahren) + ";km;" + str(
                    insgKilometer) + ";km;" + str(
                    gesamtPreis) + ";Euro;" + u1 + ";" + u2 + ";" + u3 + ";" + u4 + ";" + u5 + ";" + u6 + ";" + u7 + ";" + u8 + ";" + u9 + ";" + u10 + ";")
        print("Speichern succesfully!")

    elif Platzhalter == "n":
        print("Program beendet!")
        sys.exit(0)
