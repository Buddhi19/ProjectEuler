## Sieve of Sundaram

def generateprimes(n):

    # since we are using 2*x+2
    nN=(n-1)//2
    primes=[1 for i in range(nN+1)]

    for i in range(1,nN+1):
        j=i
        while ((i+j+2*i*j)<=nN):
            primes[i+j+2*i*j]=0
            j+=1
    arr=[]
    for i in range(1,nN+1):
        if (primes[i]==1):
            arr.append(2*i+1)
    return arr

def isHave(num):
    s=str(num)
    l=len(s)
    for i in range(1,l+1):
        if str(i) not in s:
            return False
    return True

primes=generateprimes(10**8)
print("Finished Generating")
for i in range(len(primes)):
    prime_val=primes[i]
    if isHave(prime_val):
        print(prime_val)

#7652413
