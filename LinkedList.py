## how to create manually linked list node and connect node 
# class Node:    # node object
#     def __init__(self,value):
#         self.data=value
#         self.next=None
    
# a=Node(1)
# b=Node(2)
# c=Node(3)
# print(id(a),id(b),id(c))

# a.next=b
# b.next=c
# print(b.next)


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        # to create emplty linked list -> zero nodes linked list 
        self.head=None
        self.n =0   # always tell how much node in linkd list
    
    def __len__(self):
        return self.n  # return present node 

    # // insert form Head
    def inser_Head(self,value):
        # create new Node
        new_node = Node(value)
        
        #create Connection form head or new node
        new_node.next=self.head

        #reassing head 
        self.head =new_node

        self.n+=1  # increment n
    
    def print_Node(self):
        currnet=self.head
        while currnet :   # same as current!=None
            if(currnet.next==None):
                print(currnet.data)
                break
            print(currnet.data,end="->")
            currnet=currnet.next
    
    # insert at the last 
    def insert_last(self,value):
        current=self.head
        new_node= Node(value)
        while current:
            if(current.next==None):
                current.next=new_node
                self.n+=1
                break
            current=current.next

L=LinkedList()
print(len(L))

L.inser_Head('vaibhav')
L.inser_Head('Mauli')
L.inser_Head('Gajanan')
L.inser_Head('Santosh')
print(len(L))

# travarsing linked List
L.print_Node()
L.insert_last('Sanket')
L.print_Node()