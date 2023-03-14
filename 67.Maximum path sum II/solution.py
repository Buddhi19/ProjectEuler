f=open("p067_triangle.txt")

input= lambda : f.readline().strip()

matrix=[]

arr=int(input())
matrix.append([arr])

i=0
while True:
    arr=list(map(int,input().split()))
    if len(arr)==0:
        break
    matrix.append(arr)

def maxpathsum(matrix,n):
    if n==1:
        return matrix[0][0]
    
    dp=matrix

    for i in range(n-2,-1,-1):
        for j in range(len(matrix[i])):
            dp[i][j]+=max(dp[i+1][j],dp[i+1][j+1])

    return dp[0][0]

print(maxpathsum(matrix,len(matrix)))