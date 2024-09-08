# Importiere das Modul numbers.txt als "file"
import numbers.txt as file

# Initialisiere eine leere Liste
liste = []

# Öffne die Datei im Schreibmodus ("w")
with open(file, "w") as f:
  # Lies alle Zeilen aus der Datei
  for line in f:
    # Füge jede Zeile an die Liste an
    liste.append(line)

# Drucke die Liste
print(liste)
