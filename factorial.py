def factorial(fact):
    if fact ==1 or fact ==0:
        return 1
    else:
        return fact * factorial(fact-1)

Fact = int(input("Enter the number: "))
print(factorial(Fact))