class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinekdList:
    def __init__(self):
        self.head = None

    # visiting each node one by one.
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" => ")
            temp = temp.next
        print("NULL")

    # Insertion in a Linked List
    # Insert at Beginning (O(1))
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:   # if list is empty                        
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = new_node
            # new_node.next = None


ll = LinekdList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

# visiting each node one by one.
ll.traverse()   #10 => 20 => 30 => NULL


# Insert at Beginning (O(1))
ll.insert_at_beginning(5)
ll.insert_at_end(15)
ll.traverse()   # 5 => 10 => 20 => 30 => NULL

