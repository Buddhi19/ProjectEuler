def factorial(n):
    ans=1
    for i in range(2,n+1):
        ans=ans*i

    return ans

n=int(input())
num=factorial(n)
solution=sum(map(int,str(num)))
print(solution)