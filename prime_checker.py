def is_prime(num):
  """Überprüft, ob eine Zahl eine Primzahl ist."""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def get_prime_function(prime1, prime2):
  """Erstellt eine Funktion, die mit den beiden Primzahlen multipliziert."""
  def multiply_by_primes(x):
    return x * prime1 * prime2
  return multiply_by_primes

# Eingabe der Primzahlen
prime1 = int(input("Gib die erste Primzahl ein: "))
while not is_prime(prime1):
  prime1 = int(input("Keine Primzahl. Bitte gib eine Primzahl ein: "))

prime2 = int(input("Gib die zweite Primzahl ein: "))
while not is_prime(prime2):
  prime2 = int(input("Keine Primzahl. Bitte gib eine Primzahl ein: "))

# Erstellen der Funktion
multiply_func = get_prime_function(prime1, prime2)

# Beispielhafte Verwendung
number = 5
result = multiply_func(number)
print(f"Das Ergebnis der Multiplikation von {number} mit den Primzahlen ist: {result}")
