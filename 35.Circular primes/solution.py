def circularPrime(n):
    count=1
    k = (n - 2) // 2

    marked = [False for i in range(k + 1)]
     
    SieveOfSundaram(marked, k)

    print("2", end = ' ')

    for i in range(1, k + 1):

        if (marked[i] == True):
            continue
  
        num = 2 * i + 1

        num = Rotate(num)

        while (num != 2 * i + 1):
             
            if (num % 2 == 0):
                break
  
            if (marked[(num - 1) // 2] == False):
                num = Rotate(num)
            else:
                break

        if (num == (2 * i + 1)):
            print(num, end = ' ')
            count+=1
    print()
    return count

def SieveOfSundaram(marked, k):
    for i in range(1, k + 1):
        j = i
        while (i + j + 2 * i * j) <= k:
            marked[i + j + 2 * i * j] = True
            j += 1
             
def Rotate(n):

    rem = n % 10
    rem = rem * (10 ** (countDigits(n) - 1))
    n = n // 10 
    n += rem 
    return n
 
def countDigits(n):
 
    digit =len(str(n))  
    return digit

print(circularPrime(1000000))