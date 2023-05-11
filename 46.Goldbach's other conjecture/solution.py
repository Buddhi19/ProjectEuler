

def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    
    if n%2==0 or n%3==0:
        return False
    
    for i in range(5,int(n**0.5)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
        
    return True


def findmin():
    i=3
    while True:
        if not isPrime(i):
            num=1
            while True:
                val=i-2*(num**2)
                if val<0:
                    return i
                if isPrime(val):
                    break
                num+=1
        i+=2

if __name__=="__main__":
    print(findmin())