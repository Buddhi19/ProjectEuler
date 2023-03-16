
## Function to check primes
def isPrime(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    if (n%2==0 or n%3==0):
        return False
    i=5
    while(i*i<=n):
        if (n%i==0 or n%(i+2)==0):
            return False
        i+=6
    return True

def quadratic(a,b):
    n=0
    count=0
    while True:
        num=n**2 + a*n +b
        if isPrime(num):
                count+=1
                n+=1
        else:
            return count
        
number_primes=[]
AB_product=[]

for a in range(-999,1000,1):
    for b in range(-1000,1001,1):
        if quadratic(a,b)!=0 and quadratic(a,b)!=1:
            number_primes.append(quadratic(a,b))
            AB_product.append(a*b)
            #print(number_primes[-1],end=" ")
        #print(a,b)

print(max(number_primes))
i=number_primes.index(max(number_primes))
print(AB_product[i])

# 71
# -59231