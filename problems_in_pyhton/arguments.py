def hello(x,y):
    print(f'{x} is a good {y}')

hello(y="boy", x="ramu")

def sum(a,*b):
    c=a
    for i in b:
        c=c*i
    print(c)
sum(1,2,3,4,5)
