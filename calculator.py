#calcolatrice python

num1 = float(input("scrivi il primo numero "))
operator = input("inserisci un operatore ")
num2 = float(input("srivi il secondo numero "))


if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)    
elif operator == "/":
    print(num1 / num2)
else:
    print("operatore non esistente")

    