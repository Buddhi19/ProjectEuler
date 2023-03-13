def isprime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
        
    return True

def devisors(n):
    arr=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if isprime(i):
                arr.append(i)
            large=n//i
            if isprime(large):
                arr.append(large)
    return max(arr)

n=int(input())
print(devisors(n))
