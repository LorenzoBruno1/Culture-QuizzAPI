import requests
import random

url = "https://the-trivia-api.com/api/questions" 
response = requests.get(url).json() #requette http a l'API

attempts = 3                        #varaible globale de nbr d'essai et de points
points = 0                          #variable qui vont stocker les données d'une question
categories = []
difficulty = []
question = []
correctAnswer = []
incorrectAnswers = []
for i in range(len(response)):                      #boucle qui assigne les objets au variables
    categories = response[i]['category']                    
    question = response[i]['question']
    correctAnswer = response[i]['correctAnswer'].replace('\xa0','') #remplacer par un espace les \xa0 qui apparaise desfois
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
    print("Bonne réponse !")
    attempts = attempts
    points = points + 1
elif userAnswer in incorrectAnswers :  #test si la réponse donnée est dans la list de mauvaise réponse
    print("Mauvaise réponse !")
    print("La bonne réponse était:",correctAnswer)
    attempts = attempts - 1
    points = points - 1
else:
    print("Réponse invalide")
    print("La bonne réponse était:",correctAnswer)

