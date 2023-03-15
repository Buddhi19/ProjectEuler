from num2words import num2words

t=int(input())

def letters(n):
    count=0
    for i in range(1,n+1):
        l=num2words(i)
        for character in l:
            if character==" " or character=="-":
                continue
            count+=1
    return count

print(letters(t))

