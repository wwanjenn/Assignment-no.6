# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# Steps
print('Addition Operation Quiz')
# 1 Generate random num Question, then ask for input
def scoreTally(randomNumber1, randomNumber2, answer, score):
    if randomNumber1 + randomNumber2 == answer:
    scoreCurrent = score + 1
    return scoreCurrent

# 2 Generate random number and use it on Function additionQuestion() 
# 3 Calculate Score
# 4 Print