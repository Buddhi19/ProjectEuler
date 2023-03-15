ans=0
for i in range(2,1000000):
    num=i
    sum=0
    for number in str(num):
        val=int(number)
        sum+=val**5
    if sum==num:
        print(num)
        ans+=num

print(ans)