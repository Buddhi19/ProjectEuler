#Check Pentagonal
def isPentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False


print("Started")


def sol():
    solution=[]
    for i in range(1,10**4):
        for j in range(i+1,10**4):
            val=(j-i)*(3*(j+i)-1)//2
            if isPentagonal(val):
                comb=(3*(i**2 + j**2)-(i+j))//2
                if isPentagonal(comb):
                    solution.append(val)
                    print(val)
                    print(comb,val)
                    return
sol()  
#5482660
# 8602840 5482660