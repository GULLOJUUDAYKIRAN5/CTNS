pos=-1
n=eval(input("enter any list"))
find=int(input("enter the value"))
def search(n,find):
    i=0
    while(i<len(n)):
        if(n[i]==find):
            return True
        i=i+1
        globals()['pos']=i
    return False





if(search(n,find)):
    print("found",pos)
else:
    print("not found")
   
       
