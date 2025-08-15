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
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"->",end=" ")
            temp=temp.next
    def add_at_requried_pos(self,data,pos):
        newnode=Node(data)
        temp=self.head
        x=0
        while(x!=(pos-2)):
             x+=1
             temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    
s1=single()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.insert(5)
#s1.traverse()
s1.add_at_requried_pos(100,2)
s1.traverse()


        
