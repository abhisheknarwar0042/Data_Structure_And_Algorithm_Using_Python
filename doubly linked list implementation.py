#implement doubly linked list
class doubly_linked_list_Node:
    def __init__(self,value):
        self.value=value
        self.prev_node=None
        self.next_node=None
a=doubly_linked_list_Node(1)
b=doubly_linked_list_Node(2)
c=doubly_linked_list_Node(3)
b.prev_node=a
a.next_node=b
c.prev_node=b
b.next_node=c
