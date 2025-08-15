x,y=map(int,input("enter x and y").split(""))
n=int(input("enter the year"))
if((n%100 !=0 and n%4==0) or (n%100==0 and n%400==0)):
    print(f'{n} is leap year')
else:
    print("it is not leap year")
