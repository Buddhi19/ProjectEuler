matrix=[]

while True:
    try:
        x=input()
        if x:
            matrix.append(list(map(int,x.split())))
        else:
            break
    except:
        break

maxproduct=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        up=1
        for k in range(1,5):
            try:
                up=up*(matrix[i-k][j])
            except:
                break
        if up>maxproduct:
            maxproduct=up


        down=1
        for k in range(1,5):
            try:
                down=down*(matrix[i+k][j])
            except:
                break
        if down>maxproduct:
            maxproduct=down


        sideright=1
        for k in range(1,5):
            try:
                sideright=sideright*(matrix[i][j+k])
            except:
                break
        if sideright>maxproduct:
            maxproduct=sideright


        sideleft=1
        for k in range(1,5):
            try:
                sideleft=sideleft*(matrix[i][j-k])
            except:
                break
        if sideleft>maxproduct:
            maxproduct=sideleft


        sideleftdown=1
        for k in range(1,5):
            try:
                sideleftdown=sideleftdown*(matrix[i+k][j+k])
            except:
                break
        if sideleftdown>maxproduct:
            maxproduct=sideleftdown


        sideleftup=1
        for k in range(1,5):
            try:
                sideleftup=sideleftup*(matrix[i-k][j+k])
            except:
                break
        if sideleftup>maxproduct:
            maxproduct=sideleftup


        siderightdown=1
        for k in range(1,5):
            try:
                siderightdown=siderightdown*(matrix[i+k][j-k])
            except:
                break
        if siderightdown>maxproduct:
            maxproduct=siderightdown


        siderightup=1
        for k in range(1,5):
            try:
                siderightup=siderightup*(matrix[i-k][j-k])
            except:
                break
        if siderightup>maxproduct:
            maxproduct=siderightup

print(maxproduct)