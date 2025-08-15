class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=newnode
            temp=newnode
    def traverse(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data,"->",end="")
            temp=temp.next
        print(temp.data)
    def dele_at_st(self):
        self.head=self.head.next
    def add_at_begin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

s1=single()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.traverse()
s1.dele_at_st()
s1.traverse()
s1.add_at_begin(100)
s1.traverse()





