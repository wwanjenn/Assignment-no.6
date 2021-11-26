# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)
import random
# Steps
print('Addition Operation Quiz')
# 1 Generate random num Question, then ask for input
def scoreTally(answerQuestionT, randomNumber1T, randomNumber2T, scoreT):
    if randomNumber1T + randomNumber2T == answerQuestionT:
        scoreCurrentT = scoreT + 1
    else:
        scoreCurrentT = scoreT
    return scoreCurrentT

def additionQuestion(questionNumQ, randomNumber1Q, randomNumber2Q):
    answerQuestionQ = int(input(f'{questionNumQ}. {randomNumber1Q} + {randomNumber2Q} = '))
    return answerQuestionQ

def randomGenerate():
    randomNumber1 = random.randint(0, 99)
    randomNumber2 = random.randint(0, 99)
    return randomNumber1, randomNumber2
# 2 Generate random number and use it on Function additionQuestion()
score = 0
"""No.1"""
answerQuestion = additionQuestion('1', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, score)


# 3 Calculate Score
# 4 Print
print(scoreCurrent)