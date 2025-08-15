n=int(input("enter a number"))
m=[]
while n//2!=0 or n!=1:
    m.append(int(n%2))
    n=n//2
m.append(int(n%2))
x=len(m)
for i in range(x-1,-1,-1):
    print(m[i], end=" ")
    
    
