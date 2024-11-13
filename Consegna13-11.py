print("Ciao, posso aiutarti a creare il nome per la tua band?")
risposta = input("si/no: ")
if risposta == "si":
    continuare = True
else:
    continuare = False
    if continuare:
        print("ok procediamo")
    else:
        print("Mi dispiace di non poterti aiutare =C")
        exit()
        
citta=input("inserisci il nome della tua città di origine:")
animale=input("inserisci il nome del tuo animale domestico:")

print(f"Quindi, avendo inserito questi dati il nome perfetto per la tua band è: " + citta , animale)

