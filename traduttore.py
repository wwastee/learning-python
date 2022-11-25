#trduttore giocattolo

#regole della lingua: ogni vocale diventa una "k"

def traduttore(frase):
    traduzione = ""
    for letter in frase:
        if letter in "AEIOUaeiou":
            traduzione = traduzione + "k"
        else:
            traduzione = traduzione + letter
    return(traduzione)

print(traduttore(input("inserisci una parola da tradurre: ")))