#gioco in cui bisogna indovinare una parola


print("benvenuto")

secret_word = "pinuzzo"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word: #and guess_limit <5
    guess = input("inserisci la prola ")
    guess_count += 1
    if guess_count == guess_limit:
        out_of_guesses = True
        break


if out_of_guesses == False:
    print("hai vinto")
else:
    print("hai perso")
    
    
