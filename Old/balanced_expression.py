class Stack(object):
    """
    Stack object.
    
    @param list data: a list that represents the stack.
    """
    
    def __init__(self):
        """
        Constructs a stack object.
        
        non-public varianle:
        @param list data: list that will contain the information.
        rtype: None
        """
        self.data = []
        
    def push(self, object_):
        """
        Push an object on top of the stack.
        @param Stack self: this stack.
        @param object object_: an object we are pushing on the stack.
        rtype: None
        """
        self.data.append(object_)
        
    def pop(self):
        """
        Removes an object on top of the stack and returns it.
        @param Stack self: this Stack
        rtype: object
        """
        try:
            return self.data.pop()
        except IndexError:
            print('The Stack is empty.')
    
    def is_empty(self):
        """
        Returns True if Stack is empty, false otherwise.
        @param Stack self: this stack
        rtype: bool
        """
        return len(self.data) == 0
    
    def size(self):
        """
        Returns the size of the stack.
        @param Stack self: this Stack
        rtype: int
        """
        return len(self.data)


open_brackets = '([{<' 
close_brackets = ')]}>'
    
exp = '(we[th]e)'


def is_balanced(exp, open_brackets, close_brackets):
    """ Return whether expression exp is balanced."""
    s=Stack()
    for char in exp:
        if char in open_brackets:
            s.push(open_brackets.index(char))
    for character in exp:
        if character in close_brackets:
            if s.is_empty():
                return False
            else:
                close_index = close_brackets.index(character)
                if close_index != s.pop():
                    return False
                else:
                    continue
    return s.is_empty()


print(is_balanced(exp, open_brackets, close_brackets))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    