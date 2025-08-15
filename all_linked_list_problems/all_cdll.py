class Node:
    def __init__(self,data):
        self.data=data
        self.pre=None
        self.next=None
class double:
    def __init__(self):
        self.temp=self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.temp=newnode
            newnode.next=self.head
            newnode.pre=self.head
        else:
            newnode.pre=self.temp
            self.temp.next=newnode
            self.temp=newnode
            self.temp.next=self.head
            self.head.pre=newnode 
    def traverse(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            print(self.temp.data)
            self.temp=self.temp.next
        print(self.temp.data)
d1=double()
d1.insert(1)
d1.insert(2)
d1.insert(3)
d1.insert(4)
d1.traverse()     

