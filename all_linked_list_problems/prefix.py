n=input()
stack=[]
for i in n:
    if i.isdigit():
        stack.append(int(i))
    else:
        v1=stack.pop()
        v2=stack.pop()
        if i=='+':
            stack.append(v1+v2) 
        elif i=='-':
            stack.append(v2-v1)
        elif i=='*':
            stack.append(v1*v2)
        elif i=='/':
            stack.append(v1/v2)
print(stack)



