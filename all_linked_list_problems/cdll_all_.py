class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
class double:
    def __init__(self):
        self.temp=self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.temp=self.head=newnode
            newnode.pre=self.head
            newnode.next=self.head
        else:
            newnode.pre=self.temp
            self.temp.next=newnode
            self.temp=newnode
            self.temp.next=self.head
    def traverse(self):
        self.temp=self.head
        while(self.temp.next is not self.head):
            print(self.temp.data,"<->",end="")
            self.temp=self.temp.next
        print(self.temp.data)
    def add_at_end(self,data):
        newnode=Node(data)
        self.temp=self.head
        while(self.temp.next is not self.head):
            self.temp=self.temp.next
        newnode.pre=self.temp
        self.temp.next=newnode
        newnode.next=self.head
        self.head.pre=newnode
    def add_at_begin(self,data):
        newnode=Node(data)
        self.temp=self.head
        self.temp.pre=newnode
        newnode.next=self.temp
        while self.temp.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=newnode
        self.head=newnode 
    def add_at_req_pos(self,data,index):
        newnode=Node(data)
        c=1
        self.temp=self.head
        while((index-1)>c):
            c+=1
            self.temp=self.temp.next
        self.temp.next.pre=newnode
        newnode.next=self.temp.next
        newnode.pre=self.temp
        self.temp.next=newnode
    def dele_at_end(self):
        self.temp=self.head
        while self.temp.next.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=self.head
        self.head.pre=self.temp
    def dele_at_begin(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=self.head.next
        self.head=self.head.next
        self.head.pre=self.temp
    def dele_at_req_pos(self,index):
        self.temp=self.head
        c=1
        while((index-1)>c):
            c+=1
            self.temp=self.temp.next
        self.temp.next.next.pre=self.temp
        self.temp.next=self.temp.next.next
d1=double()
d1.insert(1)
d1.insert(2)
d1.insert(3)
d1.insert(4)
d1.traverse()
d1.add_at_end(100)
d1.traverse()
d1.add_at_begin(100)
d1.traverse()
d1.add_at_req_pos(-5,3)
d1.traverse()
d1.dele_at_end()
d1.traverse()
d1.dele_at_begin()
d1.traverse()
d1.dele_at_req_pos(2)
d1.traverse()
