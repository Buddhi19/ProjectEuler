def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

paths=factorial(40)//(factorial(20)*factorial(20))

print(paths)