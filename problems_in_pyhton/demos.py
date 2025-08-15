n=eval(input("enter a number"))
max=0
for i in n:
    if i>max:
        max=i
print(f'the max element is {max}')
m=[]
for i in n:
    if i not in m:
        m.append(i)

print(m)
    
    
