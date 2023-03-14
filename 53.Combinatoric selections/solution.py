def factorial(n):
    if n==0 or n==1:
        return 1
    product=1
    for i in range(1,n+1):
        product=product*i
    return product

list1=[1 for i in range(101)]

count=0
for n in range(2,101):
    for r in range(0,n+1):
        up=factorial(n)
        list1[n]=up
        down=list1[r]*list1[n-r]
        comb=up/down
        if comb>1000000:
            count+=1
            
print(count)

