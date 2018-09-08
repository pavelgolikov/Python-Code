"""Circular Linked List."""


class _Node(object):

    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_


class CircularLinkedList:
    """
     Circular collection of LinkedListNodes
     === Attributes ==
     :param: back: the lastly appended node of this CircularLinkedList
     :type back: LinkedListNode
     """

    def __init__(self, value):
        """
         Create CircularLinkedList self with data value.
         :param value: data of the front element of this circular linked list
         :type value: object
         """
        self.back = _Node(value)
        # back.next_ corresponds to front
        self.back.next = self.back

    def __str__(self):
        """
         Return a human-friendly string representation of CircularLinkedList self
         :rtype: str
         >>> lnk = CircularLinkedList(12)
         >>> str(lnk)
         '12 ->'
         """
        # back.next_ corresponds to front
        current = self.back.next
        result = "{} ->".format(current.item)
        current = current.next
        while current is not self.back.next:
            result += " {} ->".format(current.item)
            current = current.next
        return result

    def append(self, value):
        """
         Insert value before LinkedList front, i.e. self.back.next_.
         :param value: value for new LinkedList.front
         :type value: object
         :rtype: None
         >>> lnk = CircularLinkedList(12)
         >>> lnk.append(99)
         >>> lnk.append(37)
         >>> print(lnk)
         12 -> 99 -> 37 ->
         """
        self.back.next = _Node(value, self.back.next)
        self.back = self.back.next

    def rev_print(self, current):
        if current == self.back:
            print(self.back.item)
        else:
            self.rev_print(current.next)
            print(current.item)


# cl = CircularLinkedList(12)
# cl.append(13)
# cl.append(14)
# cl.rev_print(cl.back.next)