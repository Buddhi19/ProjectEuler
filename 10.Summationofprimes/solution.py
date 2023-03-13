def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sumprimes(n):
    ans=0
    for i in range(2,n):
        if isprime(i):
            ans+=i

    return ans

n=int(input())
print(sumprimes(n))