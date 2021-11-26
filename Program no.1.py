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
def firstNumber(firstIf, secondIf, thirdIf, fourthIf):
    if firstIf >= secondIf and firstIf >= thirdIf and firstIf >= fourthIf:
        firstNumberIf = firstIf
    elif secondIf >= firstIf and secondIf >= thirdIf and secondIf >= fourthIf:
        firstNumberIf = secondIf
    elif thirdIf >= firstIf and thirdIf >= secondIf and thirdIf >= fourthIf:
        firstNumberIf = thirdIf
    elif fourthIf >= firstIf and fourthIf >= secondIf and fourthIf >= thirdIf:
        firstNumberIf = fourthIf
    return firstNumberIf
# 3 print