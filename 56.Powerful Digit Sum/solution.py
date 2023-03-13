def maxdigitsum(n):
    arr=[]
    for i in range(n):
        for j in range(n):
            digitsum=sum(map(int,str(i**j)))
            arr.append(digitsum)

    return max(arr)




n=int(input())
print(maxdigitsum(n))
