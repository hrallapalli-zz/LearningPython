number = input("Enter a non-negative integer to take a factorial of")

product = 1

for i in range(number):

    product = product*(i+1)

print(product)