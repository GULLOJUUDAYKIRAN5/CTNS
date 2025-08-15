n=int(input("enter number"))
flag=0
if n>200:
    falg=1
count=0
for i in  range(2,n//2+1):
    if(n%i==0):
        count+=1
if(count<2):
    if flag==1:
        print("prime greater than 200")
    else:
        print("prime less than 200")
    
else:
    if flag==1:
        print("not prime greater than 200")
    else:
        print(" not prime less than 200")

    