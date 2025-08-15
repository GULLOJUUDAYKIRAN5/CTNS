class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class stackLinkedlist:
        def __init__(self):
            self.top=None

        def push(self,val):
             new_node = Node(val)  
             if self.top is None:
                  self.top=new_node
                  return 
             new_node.next = self.top
             self.top = new_node
        def pop(self):
            if self.top is None:
                print("Stack is empty:")
                return
            temp = self.top.data
            self.top = self.top.next
            return temp 
        def peek(self):
            if self.top is None:
                  print("stack is empty")
                  return 
            else:
                return self.top.data
        def display(self):
            if self.top is None:
                  print("stack is empty")
            else:
                temp=self.top
                while temp:
                    print(temp.data)
                    temp=temp.next
obj=stackLinkedlist()
obj.push(1)
obj.push(2)
obj.display()
print(obj.peek())
                       
                       
              