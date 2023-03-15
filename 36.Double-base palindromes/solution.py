ans=0
def bina(n):
    num=format(n,'b')
    return num

for i in range(1000000):
    num=i
    text=str(num)
    if text==text[::-1]:
        val=bina(num)
        if val==val[::-1]:
            print(f"{num} {val}")
            ans+=num

print(ans)