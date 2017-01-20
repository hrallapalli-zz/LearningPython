# Factorial program: learning_FactorialProgram2.py

# Returns the factorial of the argument "number"
def factorial(number):

    product = 1

    for i in range(number):

        product = product * (i+1)

    return product



userInput = input("Enter a non-negative integer to take the factorial of: ")

factorial_userInput = factorial(userInput)
