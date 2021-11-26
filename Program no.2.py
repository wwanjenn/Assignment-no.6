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
        print('Correct')
    else:
        scoreCurrentT = scoreT
        print('Wrong')
    return scoreCurrentT

def additionQuestion(questionNumQ, randomNumber1Q, randomNumber2Q):
    while True:
        try:
            answerQuestionQ = int(input(f'{questionNumQ}. {randomNumber1Q} + {randomNumber2Q} = '))
            return answerQuestionQ
        except ValueError:
            print('Please enter a Valid, Whole Number')

def randomGenerate():
    randomNumber1G = random.randint(0, 99)
    randomNumber2G = random.randint(0, 99)
    return randomNumber1G, randomNumber2G
# 2 Generate random number and use it on Function additionQuestion()
scoreCurrent = 0
"""No.1"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('1', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.2"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('2', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.3"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('3', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.4"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('4', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.5"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('5', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.6"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('6', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.7"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('7', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.8"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('8', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.9"""
randomNumber1, randomNumber2= randomGenerate()
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('9', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

"""No.10"""
randomNumber1, randomNumber2= randomGenerate()
answerQuestion = additionQuestion('10', randomNumber1, randomNumber2)
scoreCurrent = scoreTally(answerQuestion, randomNumber1, randomNumber2, scoreCurrent)

# 3 Print

print(f'Your score is: {scoreCurrent}/10')