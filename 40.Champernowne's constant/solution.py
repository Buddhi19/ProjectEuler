decimal=''
i=1
while True:
    decimal+=str(i)
    i+=1
    if len(decimal)>1000000:#1000000
        break

product=1
for i in range(7):
    product=product*int(decimal[10**i-1])
    #print(10**i)


print(product)
