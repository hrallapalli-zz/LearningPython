# Returns the factorial of the argument "number" through recursion!!

def factorial(number):

    if number <=1: #base case
        return 1
    else:
        return number*factorial(number-1)



userInput = input("Enter a non-negative integer to take the factorial of: ")

factorial_userInput = factorial(userInput)

print(factorial_userInput)