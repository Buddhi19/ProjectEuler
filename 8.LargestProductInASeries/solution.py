series=''
for i in range(20):
    s=str(input())
    series+=s
arr=list(map(int,series))

ans=[]

for i in range(0,len(arr)-13):
    product=1
    for j in range(i,i+13):
        product=product*arr[j]
    ans.append(product)

print(max(ans))