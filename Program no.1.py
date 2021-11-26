# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.


# Steps

# 1 Ask for 4 numbers
def fourNumbers():
    print('Number Sorter')
    firstNumberI = float(input('First Number: '))
    secondNumberI = float(input('Second Number: '))
    thirdNumberI = float(input('Third Number: '))
    fourthNumberI = float(input('Fourth Number: '))
    return firstNumberI, secondNumberI, thirdNumberI, fourthNumberI

# 2 If else statement
def firstNumber(firstIf1, secondIf1, thirdIf1, fourthIf1):
    if firstIf1 >= secondIf1 and firstIf1 >= thirdIf1 and firstIf1 >= fourthIf1:
        firstNumberIf = firstIf1
    elif secondIf1 >= firstIf1 and secondIf1 >= thirdIf1 and secondIf1 >= fourthIf1:
            firstNumberIf = secondIf1
    elif thirdIf1 >= firstIf1 and thirdIf1 >= secondIf1 and thirdIf1 >= fourthIf1:
            firstNumberIf = thirdIf1
    else: 
        firstNumberIf = fourthIf1
    return firstNumberIf

def fourthNumber(firstIf4, secondIf4, thirdIf4, fourthIf4):
    if firstIf4 <= secondIf4 and firstIf4 <= thirdIf4 and firstIf4 <= fourthIf4:
        fourthNumberIf = firstIf4
    elif secondIf4 <= firstIf4 and secondIf4 <= thirdIf4 and secondIf4 <= fourthIf4:
            fourthNumberIf = secondIf4
    elif thirdIf4 <= firstIf4 and thirdIf4 <= secondIf4 and thirdIf4 <= fourthIf4:
            fourthNumberIf = thirdIf4
    else: 
        fourthNumberIf = fourthIf4
    return fourthNumberIf


# 3 print