c=input("enter the string")
d=['a','e','o','i','u']
n=0
for i in d:
    k=0
    for j in range(len(c)):
       if i==c[j]:
           k=k+1
    print(f' {i} occured {k} times')
            
