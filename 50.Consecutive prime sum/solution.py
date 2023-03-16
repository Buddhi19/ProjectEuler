### Sieve of sunderam

def generatePrimes(n):
    arr=[2]
    k=(n-1)//2

    primes=[True for i in range(k+1)]

    for i in range(1,k+1):
        j=i
        while ((i+j+2*i*j)<=k):
            primes[i+j+2*i*j]=False
            j+=1

    for i in range(1,k+1):
        if primes[i]==True:
            arr.append(2*i+1)

    return arr
### Check for a prime

def isPrime(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    if (n%2==0 or n%3==0):
        return False
    for i in range(5,int(n**0.5)+1,6):
        if (n%i==0 or n%(i+2)==0):
            return False
    return True

#Lets generate primes under 1000000

arr=generatePrimes(50000)
sol=[]
i=0
while i<10000:
    for j in range(50000-1,i,-1):
        updated_arr=arr[i:j]
        total=sum(updated_arr)
        if total>1000000:
            continue
        if isPrime(total):
            sol.append(total)
            print(total)
            break
    i+=1

print(sol)
print(max(sol))

#997651



