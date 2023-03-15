
triangular=[i*(i+1)//2 for i in range(1,10000)]

f=open("p042_words.txt")

input=lambda : f.readline().strip()

arr=list(map(str,input().split(",")))

count=0

#64

for i in range(len(arr)):
    name=arr[i]
    sum=0
    for character in name:
        if character!='"':
            sum+=ord(character)-64
    if sum in triangular:
        print(name)
        count+=1

print(count)
# print(ord("Y")-64)