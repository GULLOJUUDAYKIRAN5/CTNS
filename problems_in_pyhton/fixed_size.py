class stack:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top==self.size-1
    def push(self,item):
        if self.isFull():
            print("stack is full")
            return
        else:
            self.top+=1
            self.stack[self.top]=item
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            temp=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return temp
    def peek(self):
        if self.isEmpty():
            print("is empty")
            return
        else:
            return self.stack[self.top]
    def display(self):
        if self.isEmpty():
            return
        else:
            return self.stack
obj=stack(5)
obj.push(5)
obj.push(10)
print(obj.display())
obj.pop()
print(obj.display())
