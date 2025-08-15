class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
class double:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def traverse(self):
        self.temp=self.head
        while self.temp.next is not None:
            print(self.temp.data)
            self.temp=self.temp.next
d1=double()
d1.insert(2)
d1.insert(3)
d1.insert(4)
d1.traverse()