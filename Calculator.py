def add(x, y):
    """Führt die Addition von zwei Zahlen durch."""
    return x + y

def subtract(x, y):
    """Führt die Subtraktion von zwei Zahlen durch."""
    return x - y

def multiply(x, y):
    """Führt die Multiplikation von zwei Zahlen durch."""
    return x * y

def divide(x, y):
    """Führt die Division von zwei Zahlen durch. Gibt eine Fehlermeldung zurück, wenn der Divisor Null ist."""
    if y != 0:
        return x / y
    else:
        return "Fehler: Division durch Null"

def main():
    """Hauptfunktion des Taschenrechners."""
    while True:
        print("\nWählen Sie eine Operation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Beenden")
        
        choice = input("Geben Sie Ihre Wahl (1/2/3/4/5): ")

        if choice == '5':
            print("Programm beendet.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Geben Sie die erste Zahl ein: "))
                num2 = float(input("Geben Sie die zweite Zahl ein: "))
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                continue

            if choice == '1':
                print(f"Ergebnis: {add(num1, num2)}")

            elif choice == '2':
                print(f"Ergebnis: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Ergebnis: {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"Ergebnis: {result}")

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")

if __name__ == "__main__":
    main()
