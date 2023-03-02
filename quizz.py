import requests
import random

url = "https://the-trivia-api.com/api/questions" 
response = requests.get(url).json() #requette http a l'API

#variable qui vont stocker les données d'une question
categories = []
difficulty = []
question = []
correctAnswer = []
incorrectAnswers = []
points = 0
i = 0
round = 0
while round < 10 and i < len(response):                      #boucle qui assigne les objets au variables
    categories = response[i]['category']                    
    question = response[i]['question']
    correctAnswer = response[i]['correctAnswer'].replace('\xa0', '')#remplacer par un espace les \xa0 qui apparaise desfois
    incorrectAnswers = response[i]['incorrectAnswers']


    allAnswers = [correctAnswer] + incorrectAnswers     #variable contenant toute les réponses
    random.shuffle(allAnswers)                          #mélange de l'ordre des réponses

    if 'difficulty' in response[i]:
        difficulty = response[i]['difficulty']
        print (f"{categories}, {difficulty}\n \n{question}\n{allAnswers}")
    else:
        print (f"{categories},\n{question}\n{allAnswers}") #affichage catégorie , difficulté,question,réponse proposé
        
    userAnswer = input("")
    if(userAnswer == correctAnswer):
        points = points + 1
        round = round + 1
        i += 1
        print("Bonne réponse !")
        print("Vous avez:",points,"/",round,"Réponse correct")
    elif userAnswer in incorrectAnswers :  #test si la réponse donnée est dans la list de mauvaise réponse
        round = round + 1
        i += 1
        print("Mauvaise réponse !")
        print("La bonne réponse était:",correctAnswer)
        print("Vous avez:",points,"/",round,"Réponse correct")
    else:
        i += 1
        round = round + 1
        print("Réponse invalide !")
        print("La bonne réponse était:",correctAnswer)
        print("Vous avez:",points,"/",round,"Réponse correct")


