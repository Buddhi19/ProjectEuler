num=1
while True:
    numarray=list(str(num))
    k=0
    for i in range(2,7):
        product=i*num
        for number in str(product):
            if number not in numarray:
                k+=1
                continue

    if k==0:
        print(num)
        break
    num+=1
    