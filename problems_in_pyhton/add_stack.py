s1=[]
s2=[]
carry=0
res=[]
n1=input()
n2=input()
for i in n1:
    s1.append(i)
for j in n2:
    s2.append(j)
while s1 or s2 or carry:
    if s1:
        dig1=s1.pop()
    else:
        dig1=str(0)
    if s2:
        dig2=s2.pop()
    else:
        dig2=str(0)
    tot=int(dig1)+int(dig2)+carry
    
    res.append(str(tot%10))
    carry=(tot)//10
print(''.join(res[::-1]))

