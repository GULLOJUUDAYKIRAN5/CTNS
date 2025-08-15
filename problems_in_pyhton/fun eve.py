
def count(list):
    e=0
    o=0
    for i in list:
        if(i%2==0):
            e=e+1
        else:
            o=o+1
    return e,o


list=eval(input("enter the list"))
e,o=count(list)
print(f'even is {e} and odd is {o}')
