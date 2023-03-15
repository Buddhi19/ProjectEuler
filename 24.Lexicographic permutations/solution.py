from itertools import permutations

arr=[0,1,2,3,4,5,6,7,8,9]

solution=permutations(arr)

n=1000000

ans=list(solution)[n-1]

for i in range(10):
    print(ans[i],end="")