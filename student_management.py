import csv

# Erstellen eines Dictionaries, um Schülerdaten nach Matrikelnummer zu speichern
schueler_duesseldorf = {}

# Öffnen der CSV-Datei mit den Schülerdaten
with open("schule_düsseldorf.csv", "r") as datei:
    # Erstellen eines CSV-Lesers, der jede Zeile als Dictionary behandelt
    schueler_leser = csv.DictReader(datei)

    # Durchlaufen jeder Zeile (jeden Schülers) in der CSV-Datei
    for schueler in schüler_leser:
        # Extrahieren der Matrikelnummer aus dem aktuellen Schüler-Datensatz
        matrikelnummer = schüler["Matrikelnummer"]
        # Entfernen der Matrikelnummer aus dem Schüler-Datensatz, da sie als Schlüssel verwendet wird
        del schüler["Matrikelnummer"]
        # Hinzufügen des Schülers zum Schülerverzeichnis mit der Matrikelnummer als Schlüssel
        schueler_duesseldorf[matrikelnummer] = schüler

# Ausgabe des gesamten Schülerverzeichnisses
print(schueler_duesseldorf)
