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
            self.temp=self.head=newnode
            newnode.pre=self.head
        else:
            newnode.pre=self.temp
            self.temp.next=newnode
            self.temp=newnode
    def traverse(self):
        self.temp=self.head
        while self.temp.next is not None:
            print(self.temp.data,"<->",end="")
            self.temp=self.temp.next
        print(self.temp.data)
    def add_at_end(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head=newnode
            newnode.pre=self.head
        else:
            self.temp=self.head
            while(self.temp.next is not None):
                self.temp=self.temp.next
            newnode.pre=self.temp
            self.temp.next=newnode
    def add_at_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.pre=self.head
        else:
            self.temp=self.head
            self.temp.pre=newnode
            newnode.next=self.temp
            self.head=newnode
    def  add_at_req(self,data,index):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.pre=self.head
        else:
            self.temp=self.head
            c=1
            while((index-1)>c):
                self.temp=self.temp.next
                c+=1
            self.temp.next.pre=newnode
            newnode.next=self.temp.next
            newnode.pre=self.temp
            self.temp.next=newnode
    def dele_at_end(self):
        self.temp=self.head
        while self.temp.next.next is not None:
            self.temp=self.temp.next 
        self.temp.next=None
    def dele_at_begin(self):
        self.temp=self.head
        self.head=self.temp.next
        self.temp.next.pre=self.head
    def del_at_req(self,index):
        c=1
        self.temp=self.head
        while((index-1)>c):
            c+=1
            self.temp=self.temp.next
        self.temp.next.next.pre=self.temp
        self.temp.next=self.temp.next.next
d1=double()
d1.insert(1)
d1.insert(2)
d1.insert(3)
d1.add_at_end(100)
d1.add_at_begin(200)
d1.add_at_req(500,3)
d1.traverse()
d1.dele_at_end()
d1.traverse()
d1.dele_at_begin()
d1.traverse()
d1.del_at_req(3)
d1.traverse()
    
