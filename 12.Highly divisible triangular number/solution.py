def numberofdevisors(n):
    count=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if n//i==i:
                count+=1
            else:
                count+=2
    return count

def triangular(n):
    num=n*(n+1)//2
    return num

n=int(input())
number=1
while True:
    tri=triangular(number)
    devisors=numberofdevisors(tri)
    if devisors>=n:
        print(tri)
        break
    number+=1