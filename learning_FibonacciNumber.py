# Fibonacci numbers are 0,1,1,2,3,5,8,13.... The ratio of n-1 to n gives the golden ratio

def Fibonacci(n):  # Returns the n-th Fibonacci number 
    i = 0
    FibSeq = [0,1] # Base cases... there must be a better way to do this
    if n <= 2:
        return FibSeq[n-1]
    else:
        while i<n:
            FibSeq.append(FibSeq[i]+FibSeq[i+1]) # Expensive list of all of the numbers in the list. I don't know how to store previous values in memory while dropping old, unnecessary values.
            i = i+1
        return FibSeq[n-1]

userInput = input("Enter the term of the Fibonacci sequence: ")

Fibonacci_userInput = Fibonacci(userInput)

print(Fibonacci_userInput)
