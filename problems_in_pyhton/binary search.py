pos=-1
lis=eval(input("enter the list"))
n=int(input("enter the value"))
def search(lis,n):
    lb=0
    ub=len(lis)-1
    while(lb<=ub):
        mid=(lb+ub)//2
        if(lis[mid]==n):
            globals()['pos']=mid
            return True
        else:
            if(lis[lb]<n):
                lb=mid+1
            else:
                ub=mid-1
    return False



if search(lis,n):
    print("found",pos)
else:
    print("not found")
