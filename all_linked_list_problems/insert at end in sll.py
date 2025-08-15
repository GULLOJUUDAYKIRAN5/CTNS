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
            print(self.head.data)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
            temp=newnode
    def insert_end(self,data):
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
            print(temp.data)
            temp=temp.next
s1=single()
s1.insert(1)
# s1.insert(2)
# s1.insert(3)
# #s1.traverse()
# s1.insert_end(100)
# s1.traverse()


        