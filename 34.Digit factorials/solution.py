
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
ans=0
for i in range(3,100000):
    num=i
    sum=0
    for number in str(num):
        sum+=factorial(int(number))

    if sum==num:
        ans+=num
        print(sum)

print(ans)
