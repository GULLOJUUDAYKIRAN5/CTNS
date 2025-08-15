import random as r
import string as s
n=int(input("enter the length of the pass"))
l=s.digits+s.punctuation+s.ascii_letters
password=[]
print(r.choice(l))
for i in range(n):
    password.append((r.choice(l)))
print(password)

