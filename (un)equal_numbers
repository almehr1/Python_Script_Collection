zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gerade_zahlen, ungerade_anzahl = filter_gerade_zahlen(zahlen)

print(gerade_zahlen)  # Ausgabe: [2, 4, 6, 8]
print(ungerade_anzahl)  # Ausgabe: 5

def filter_gerade_zahlen(zahlen):
  """
  Filtert eine Liste von Zahlen und gibt eine neue Liste mit den geraden Zahlen zurück.

  Args:
    zahlen: Eine Liste von Zahlen.

  Returns:
    Ein Tupel aus zwei Elementen:
    - Eine neue Liste mit den geraden Zahlen.
    - Die Anzahl der ungeraden Zahlen.
  """

  gerade = []
  ungerade = 0
  for zahl in zahlen:
    if zahl % 2 == 0:
      gerade.append(zahl)
    else:
      ungerade += 1
  return gerade, ungerade
