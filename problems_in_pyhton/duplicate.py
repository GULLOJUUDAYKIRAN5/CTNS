li=[1,23,4,4,5]
vi=[5,5,4,3,2,1]
for i,j in zip(set(li),set(vi)):
    print(f'{i} is the {j}')
k=[1,2,2,3]
l=set(li)
for i,j in zip(k,l):
    print(f'{i} and {j}')