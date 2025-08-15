class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
            temp=newnode
    def dele_at_req(self,pos):
        temp=self.head
        c=1
        while((pos-1)!=c):
            c+=1
            temp=temp.next
        temp.next=temp.next.next
    def traverse(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data,"->",end="")
            temp=temp.next
        print(temp.data)
s1=single()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.insert(5)
s1.traverse()
s1.dele_at_req(4)
s1.traverse()

        