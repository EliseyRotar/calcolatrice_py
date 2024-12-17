while True:
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta int(input("1) sottrazione\n2)addizione\n0)exit\n"))
    if scelta==0:
        break
    if scelta == 3:
        print("Grazie per aver usato la calcolatrice. Arrivederci!")
        break
    elif scelta == 1:
        sottrazione()
    elif scelta == 2:
        somma()
    else:
        print("Scelta non corretta!")
