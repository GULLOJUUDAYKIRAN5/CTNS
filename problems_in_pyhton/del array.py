from array import *
n=int(input("enter a value"))
arr=array('i',[])
arr1=array('i',[])

for i in range(n):
    x=int(input("enter a value"))
    arr.append(x)
print(arr)
for i in range(n):
    if i==2:
        arr.pop(i)
        '''arr.remove(n[i])'''
for i in range(n-1-1):
    if i==2:
        arr1.append(arr[i+1])
    else:
        arr1.append(arr[i])
        
print(arr)
print(arr1)
