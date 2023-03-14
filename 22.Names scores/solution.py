f=open("p022_names.txt")

input= lambda: f.readline().strip()



arr=list(input().split(","))
arr.sort()
score=0

def namevalue(name):
    value=0
    for character in range(1,len(name)-1):
        value+=ord(name[character])-64
        #print(name[character])
    return value


for i in range(len(arr)):
    namescore=namevalue(arr[i])*(i+1)
    score+=namescore
    #print(f"{i}-{score}")

print(score)
