n=eval(input("enter the list"))
m=len(n)
p=n[0]
n[0]=n[m-1]
n[m-1]=p
print(n)
