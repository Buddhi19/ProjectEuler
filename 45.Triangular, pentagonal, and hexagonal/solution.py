triangular=[]
pentagonal=[]
hexagonal=[]

i=1
count=0
while True:
    t=i*(i+1)/2
    triangular.append(t)
    p=i*(3*i -1)/2
    pentagonal.append(p)
    h=i*(2*i -1)
    hexagonal.append(h)

    if t in pentagonal and t in hexagonal:
        print(t)
        count+=1

    i+=1
    if count==3:
        break
