#questo è un gioco a quiz che fa uso di una classe
from domande import Question

question_prompt = [
    "Di che colore sono le mele? \n(a) Rosse/Verdi \n(b) Viola \n(c) Arancioni \n\n",
    "Di che colore sono le banane? \n(a) Azzurre \n(b) Magenta \n(c) Gialle \n\n",
    "Di che colore sono le ciliegie? \n(a) Blu \n(b) Nere \n(c) Rosse \n\n"
]

questions =[
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c"),
]

def run_test(questions):
    score=0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("ne hai azzeccate "+ str(score) +"/"+ str(len(questions)))

run_test(questions)