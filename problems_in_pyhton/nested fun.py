def s1():
     u='uday'
     def s2():
         g='kiran'
         print(u)
         def s3():
             print(u)
             print(g)
         s3()
     s2()
s1()
#"""in function the inner function can access the data of the outer function but not vise versa """
