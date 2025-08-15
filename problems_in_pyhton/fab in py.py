def fab(n):
    a=0
    b=1
    print (f'{a} \n {b}')
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(c)
def fabu(n,x,list):
    a=0
    b=1
    list.append(a)
    list.append(b)
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        list.append(c)
    print(list)
    print(list[x-1])
    
n=int(input("enter the n value"))
fab(n)
x=int(input("enter the x value"))
list=[]
fabu(n,x,list)


