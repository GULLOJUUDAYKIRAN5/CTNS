import time
x=int(input("enter the noof seconds"))
for i in reversed(range(0,x)):
    print(i)
    time.sleep(1)
print("the time is complted")
