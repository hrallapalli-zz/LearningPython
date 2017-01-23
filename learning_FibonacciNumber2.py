# Fibonacci numbers are 0,1,1,2,3,5,8,13.... The ratio of n-1 to n gives the golden ratio

def Fibonacci(n):  # Returns the n-th Fibonacci number 
    i = 0
    FibSeq = [0,1] # Base cases.

    while i<n-1:
            FibSeq = [FibSeq[1], FibSeq[0]+FibSeq[1]] # Clean and memory frugal storage
            i=i+1
    return FibSeq[0]

userInput = input("Enter the term of the Fibonacci sequence: ")

Fibonacci_userInput = Fibonacci(userInput)

print(Fibonacci_userInput)
    