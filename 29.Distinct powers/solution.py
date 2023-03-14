list1=[]
for i in range(2,101):
    for j in range(2,101):
        val=i**j
        if val not in list1:
            list1.append(val)

print(len(list1))