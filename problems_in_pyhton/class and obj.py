class student:
    def behv(self):
        print("only few are good")

class teacher:
    def exp(self):
        print("only few have exp")

s1=student()
s2=student()
t1=teacher()

s1.behv()
t1.exp()
student.behv(s2)
