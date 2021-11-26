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

def secondNumber(firstIf2, secondIf2, thirdIf2, fourthIf2):
    if firstIf2 <= secondIf2 and firstIf2 >= thirdIf2 and firstIf2 >= fourthIf2:
        secondNumberIf = firstIf2
    elif firstIf2 >= secondIf2 and firstIf2 <= thirdIf2 and firstIf2 >= fourthIf2:
        secondNumberIf = firstIf2
    elif   firstIf2 >= secondIf2 and firstIf2 >= thirdIf2 and firstIf2 <= fourthIf2:
        secondNumberIf = firstIf2
    
    if secondIf2 <= firstIf2 and secondIf2 >= thirdIf2 and secondIf2 >= fourthIf2:
            secondNumberIf = secondIf2
    elif secondIf2 >= firstIf2 and secondIf2 <= thirdIf2 and secondIf2 >= fourthIf2:
            secondNumberIf = secondIf2
    elif secondIf2 >= firstIf2 and secondIf2 >= thirdIf2 and secondIf2 <= fourthIf2:
            secondNumberIf = secondIf2

    if thirdIf2 <= firstIf2 and thirdIf2 >= secondIf2 and thirdIf2 >= fourthIf2:
            secondNumberIf = thirdIf2
    elif thirdIf2 >= firstIf2 and thirdIf2 <= secondIf2 and thirdIf2 >= fourthIf2:
            secondNumberIf = thirdIf2
    elif thirdIf2 >= firstIf2 and thirdIf2 >= secondIf2 and thirdIf2 <= fourthIf2:
            secondNumberIf = thirdIf2
    
    else: 
        secondNumberIf = fourthIf2
    return secondNumberIf

def thirdNumber(firstIf3, secondIf3, thirdIf3, fourthIf3):
    if firstIf3 >= secondIf3 and firstIf3 <= thirdIf3 and firstIf3 <= fourthIf3:
        thirdNumberIf = firstIf3
    elif firstIf3 <= secondIf3 and firstIf3 >= thirdIf3 and firstIf3 <= fourthIf3:
        thirdNumberIf = firstIf3
    elif firstIf3 <= secondIf3 and firstIf3 <= thirdIf3 and firstIf3 >= fourthIf3:
        thirdNumberIf = firstIf3

    if secondIf3 >= firstIf3 and secondIf3 <= thirdIf3 and secondIf3 <= fourthIf3:
            thirdNumberIf = secondIf3
    elif secondIf3 <= firstIf3 and secondIf3 >= thirdIf3 and secondIf3 <= fourthIf3:
            thirdNumberIf = secondIf3
    elif secondIf3 <= firstIf3 and secondIf3 <= thirdIf3 and secondIf3 >= fourthIf3:
            thirdNumberIf = secondIf3
    
    if thirdIf3 >= firstIf3 and thirdIf3 <= secondIf3 and thirdIf3 <= fourthIf3:
            thirdNumberIf = thirdIf3
    elif thirdIf3 <= firstIf3 and thirdIf3 >= secondIf3 and thirdIf3 <= fourthIf3:
            thirdNumberIf = thirdIf3
    elif thirdIf3 <= firstIf3 and thirdIf3 <= secondIf3 and thirdIf3 >= fourthIf3:
            thirdNumberIf = thirdIf3

    else:
        thirdNumberIf = fourthIf3
    return thirdNumberIf

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