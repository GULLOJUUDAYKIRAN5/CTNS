nums=list(input("enter list"))
target=int(input("enter the target"))
y=[]
x=len(nums)
for i in range(0,x):
    for j in range(i+1,x):
        if((nums[i]+nums[j])==target):
            print(i,j)
