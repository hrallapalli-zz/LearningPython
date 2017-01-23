# This code returns the n-th Fibonacci number


def Fibonacci(n):
    FibSeq = [0,1] # Base case
    # i = n
    if n <=1:
        return FibSeq[n]
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


userInput = input("Enter the term of the Fibonacci sequence: ")

Fibonacci_userInput = Fibonacci(userInput)

print(Fibonacci_userInput)
    