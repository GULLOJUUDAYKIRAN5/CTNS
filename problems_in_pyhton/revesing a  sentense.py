s=input("enter a sentence")
p=s.split()[::-1]
print(p)
l=[]
for i in p:
    l.append(i)
print(l)
for i in p:
    print(i,end=" ")
