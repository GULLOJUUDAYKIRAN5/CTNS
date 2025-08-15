for i in range(7):
    for j in range(5):
        if i==0 and j in {0,1,2,3,4}:
           print("*",end=" ")
        elif i in {1,2,4,5,6} and j in {0,4}:
           print("*",end=" ")
        elif i==3:
           print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
