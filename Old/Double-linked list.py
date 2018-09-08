class Node(object):
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        self.previous = None
        
    def __str__(self):
        
        return str(self.data)


class DoubleLinkedList(object):
    
    def __init__(self):
        
        self.head =  None
        
    def add(self, o):
        
        node = Node(o)
        if self.head == None:
            self.head = node
            self.head.next = None
            self.head.previous = None
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        
        
    def __str__(self):
        tot = ''
        count = self.head
        while count != None:
            tot += str(count.data) + ' <-> '
            count = count.next
        return tot[:-5]
    
    
C = DoubleLinkedList()

C.add(1)
C.add('Bob')
C.add([1,2,56, {'f': 32}])
C.add('Denis') 












