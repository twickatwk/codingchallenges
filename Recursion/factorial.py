def factorial(n):
    print("Factorial(" + str(n) +")")
    if n == 0:
        return 1
    else:
        f = n * factorial(n-1)
        print("value of F(" + str(n) + "): " + str(f))
        return f
print(factorial(4))