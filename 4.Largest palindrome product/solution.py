def ispalindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    return False

ans=[]
for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        if ispalindrome(num):
            ans.append(num)

print(max(ans))