class Node(object):
    '''
    Represents a node of the queue.

    @param object data: info to be kept inside this node.
    '''

    def __init__(self, data):
        '''
        Creates a TNode object.

        @param Node self: this TNode
        @param object data: info to be kept inside this node.
        rtype: None
        '''
        self.data = data
        self.next = None

    def get_data(self):
        '''
        Returns data = info kept in the node

        @param Node self: this TNode
        rtype: object
        '''
        return self.data

    def get_next(self):
        '''
        Returns the next TNode.

        @param Node self: this TNode
        rtype: object
        '''
        return self.next

    def set_next(self, o):
        '''
        Sets the next node

        @param Node self: this TNode
        @param object o: object to be put into the next TNode.
        rtype: none
        '''
        self.next = o

    def __str__(self):
        '''
        Prints a string representation of this TNode, which is just its data.

        @param Node self: this TNode
        rtype: str
        '''
        return str((self.data))


class Queue(object):
    '''
    Represents a Queue

    @param object data
    '''

    def __init__(self):
        '''
        Creates a Queue with first element as TNode containing data object.

        @param Queue self: this Queue
        rtype: None
        '''
        self.head = None
        self.tail = self.head

    def push(self, o):
        '''
        Pushes a TNode with object o on top of the Queue.

        @param Queue self: this Queue
        @param object o: object to be pushed on top of the Queue.
        rtype: None
        '''
        node_o = Node(o)
        if self.head == None:
            self.head = node_o
            self.tail = node_o
            self.head.set_next(self.tail)
        else:
            self.tail.set_next(node_o)
            self.tail = node_o

    def pop(self):
        '''
        Removes the tail node of the Queue and returns it.

        @param Queue self: this Queue
        rtype: TNode
        '''
        res = self.head
        self.head = self.head.get_next()
        return res

    def size(self):
        '''
        Returns the number of elements in the Queue.

        @param Queue self: this Queue
        rtype: int
        '''
        res = self.head
        counter = 0
        while res != None:
            res = res.get_next()
            counter += 1
        return counter

    def is_empty(self):
        '''
        Returns True if this Queue is empty and False otherwise.

        @param Queue self: this Queue
        rtype: bool
        '''
        try:
            self.head.get_data()
        except AttributeError:
            return True
        return False


Q = Queue()
Q.push(2)
Q.push(3)
Q.push(4)
Q.push(5)
