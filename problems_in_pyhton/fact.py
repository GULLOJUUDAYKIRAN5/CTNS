n=5
sum=1
while(n>0):
    sum=sum*n
    n-=1
print(sum)


m=5
def sum(n):
    if(n==0):
        print(n)
    else:
        n=n*(n-1)
        sum(n-1)
sum(m)
