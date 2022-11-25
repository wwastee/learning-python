#calcolatrice python


while True:
    try:
        num1 = float(input("scrivi il primo numero "))
        operator = input("inserisci un operatore ")
        num2 = float(input("srivi il secondo numero "))



        if operator == "+":
            print (num1 + num2)
            break
        elif operator == "-":
            print (num1 - num2)
            break
        elif operator == "*":
            print (num1 * num2)    
            break
        elif operator == "/":
            print(num1 / num2)
            break
        else:
            print("operatore non esistente")
    except:
        print("imput invalido, inserisci un numero")

        