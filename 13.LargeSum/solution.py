def largesum(Matrix,step,currentsum):
    tempsum=currentsum
    if step>=50:
        return currentsum
    for i in range(len(Matrix)):
        number=int(str("".join(str(x) for x in Matrix[i][(40-step):(50-step)])))
        tempsum+=number
    if step!=40:
        currentsum=tempsum//10**10   
    else:
        currentsum=tempsum
    return largesum(Matrix,step+10,currentsum)

t=int(input())
Matrix=[]
for _ in range(t):
    s=str(input())
    arr=[]
    for i in range(50):
        arr.append(s[i])
    Matrix.append(arr)

print(str(largesum(Matrix,0,0))[:10])

#5537376230