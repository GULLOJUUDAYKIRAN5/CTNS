class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circular:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.temp=newnode
            self.head.next=self.head
        else:
            self.temp.next=newnode
            self.temp=newnode
            self.temp.next=self.head
    def add_at_end(self,data):
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=newnode
        newnode.next=self.head
    def add_at_st(self,data):
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not self.head: 
            self.temp=self.temp.next
        self.temp.next=newnode
        newnode.next=self.head
        self.head=newnode 
    def display(self):
        self.temp=self.head
        while(self.temp.next is not self.head):
            print(self.temp.data,"->",end="")
            self.temp=self.temp.next
        print(self.temp.data)
    def add_at_req_pos(self,data,index):
        newnode=Node(data)
        self.temp=self.head
        c=1
        while((index-1)>c):
            self.temp=self.temp.next
            c+=1
        newnode.next=self.temp.next
        self.temp.next=newnode
    def dele_at_end(self):
        self.temp=self.head
        while self.temp.next.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=self.head
    def dele_at_st(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            self.temp=self.temp.next
        self.temp.next=self.head.next
        self.temp=self.head
        self.head=self.temp.next

    def dele_at_req_pos(self,index):
        self.temp=self.head
        c=1
        while((index-1)>c):
            self.temp=self.temp.next
            c+=1
        self.temp.next=self.temp.next.next
c1=circular()
c1.insert(1)
c1.insert(2)
c1.insert(3)
c1.display()
c1.add_at_end(100)
c1.add_at_st(200)
c1.add_at_req_pos(1000,2)
c1.display()
c1.dele_at_end()
c1.display()
c1.dele_at_st()
c1.display()
c1.dele_at_req_pos(2)
c1.display()

        
