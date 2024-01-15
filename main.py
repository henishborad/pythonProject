def factorial(num=int(input("Enter num: "))):
    fact = 1
    if num < 0:
        print("Invalid")
    if num == 0:
        print("Factorial of 0 is 1.")
    if num > 0:
        for i in range(1, num + 1):
            fact = fact * i
        print(f"Factorial of {num} is {fact}.")
    return fact


factorial()
