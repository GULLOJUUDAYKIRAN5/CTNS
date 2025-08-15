l=[10,9,4,3,2,4,2]
f=len(l)
for i in range(f-1,0,-1):
    for j in range(i):
        if(l[j]>l[j+1]):
            temp=l[j+1]
            l[j+1]=l[j]
            l[j]=temp

print(l)
