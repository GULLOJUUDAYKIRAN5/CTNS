from array import*
n=int(input("enter lenght"))
arr=array('i',[])
for i in range(n):
    x=int(input("enter the array elements"))
    arr.append(x)
print(arr)
p=int(input("enter a value"))
for i in range(len(arr)):
    if p==arr[i]:
        print(i)
