s1=int(input("enter the sub marks"))
s2=int(input("enter the sub marks"))
s3=int(input("enter the sub marks"))
s4=int(input("enter the sub marks"))
s5=int(input("enter the sub marks"))
s6=int(input("enter the sub marks"))
avg=(s1+s2+s3+s4+s5+s6)/6
if(s1>40 and s2>40 and s3>40 and s4>40 and s5>40 and s6>40 and avg<=90 and avg>=80 ):
    print("A GRADE")
elif(s1>40 and s2>40 and s3>40 and s4>40 and s5>40 and s6>40 and avg<79 and avg>70 ):
    print("B GRADE")
elif(s1>40 and s2>40 and s3>40 and s4>40 and s5>40 and s6>40 and avg<69 and avg>60 ):
    print("C GRADE")
elif(s1>40 and s2>40 and s3>40 and s4>40 and s5>40 and s6>40 and avg<59 and avg>51 ):
    print("D GRADE")
else:
    print("FAIL")
