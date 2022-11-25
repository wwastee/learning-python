#funzione che eleva alla potenza un numero


def alla_potenza(numero, potenza):
    risultato=1
    for index in range(potenza):
        risultato = risultato * numero
    return risultato

num1 = int(input("scrivi il numero base "))
num2 = int(input("scrivi la potenza a cui vuoi elevarlo "))

print(alla_potenza(num1, num2))