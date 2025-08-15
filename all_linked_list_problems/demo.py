class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=temp=newnode
        else:
            temp.next=newnode
            temp=newnode
    def traverse(self):
        if(self.head==None):
            print("list is empty")
        else:
            temp=self.head
            while(temp.next!=None):
                print(temp.data)
                temp=temp.next
s1=single()
s1.insert(10)
s1.insert(11)
s1.traverse()
