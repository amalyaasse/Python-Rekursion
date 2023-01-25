def Fakult(n): # Funktion zum aufsummieren die zahlen 1 bis n
    if n == 1:
        return 1
    else:
        return n * Fakult(n - 1)
    
zahl = int(input("Bitte Ganzzahl n eingeben: "))
ergebnis = Fakult(zahl)
print(ergebnis)