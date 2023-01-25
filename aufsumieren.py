def aufsu(n): # Funktion zum aufsummieren die zahlen 1 bis n
    if n == 0:
        return 0
    else:
        return n + aufsu(n - 1)
    
zahl = int(input("Bitte Ganzzahl n eingeben: "))
ergebnis = aufsu(zahl)
print(ergebnis)