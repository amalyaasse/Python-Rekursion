def schneiden(durchmesser):
    if durchmesser > 1:
        durchmesser = durchmesser -1
        print("Axtschlag: Baum fällen.")
        schneiden(durchmesser)
    else:
        print("Baum gefällt")

Startwert_durchmesser = 5
schneiden(Startwert_durchmesser)