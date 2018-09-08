"""Linked List Implementation with several functions."""


class _Node(object):
    """Linked List node."""
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_

    def __str__(self):
        return str(self.item)


class LinkedList(object):
    """Linked List Class."""
    def __init__(self):
        """Create an instance of Linked List"""
        self.front = None
        self.size = 0
        self._iterator = None

    def __len__(self):
        """Return the length of Linked List self."""
        if self.front == None:
            return 0
        else:
            count = 1
            curr = self.front
            while curr.next:
                count += 1
                curr = curr.next
            return count

    def __str__(self):
        """Return a string representation of Linked List self."""
        if self == None:
            return ''
        else:
            curr = self.front
            s = ''
            while curr:
                s += str(curr.item) + ' '
                curr = curr.next
            return s

    def add(self, el):
        """Add node with el as value into Linked List self."""
        if self.front == None:
            self.front = _Node(el)
        else:
            curr = self.front
            while curr.next:
                curr = curr.next
            curr.next = _Node(el)
        self.size += 1

    def __contains__(self, el):
        """Return whether self contains node with el as value"""
        if self.front == None:
            return False
        else:

            curr = self.front
            while curr:
                if curr.item == el:
                    return True
                else:
                    curr = curr.next
            if curr == None:
                return False

    def __getitem__(self, ind):
        """Return an item at index ind. Raise error if index is out of bounds."""
        if self.front == None:
            raise IndexError
        else:

            curr = self.front
            count = 0

            while curr:
                if count == ind:
                    return curr.item
                count += 1
                curr = curr.next
            if curr == None:
                raise IndexError

    def __setitem__(self, ind, el):
        """Set item at index ind to have value el. Raise error if index is out of bounds."""
        if self.front == None:
            raise IndexError
        else:

            curr = self.front
            count = 0
            while curr:
                if count == ind:
                    curr.item = el
                    return
                count += 1
                curr = curr.next
            if curr == None:
                raise IndexError

    def insert(self, ind, el):
        if ind < 0 or ind > (len(self) - 1):
            raise IndexError
        else:
            if ind == 0:
                new_node = _Node(el)
                new_node.next = self.front
                self.front = new_node
            else:
                count = 0
                curr = self.front
                while curr:
                    if count == ind - 1:
                        new_node = _Node(el)
                        new_node.next = curr.next
                        curr.next = new_node
                        break
                    count += 1
                    curr = curr.next

    def remove(self, ind):
        if self.front == None:
            raise IndexError
        else:
            if ind == 0:
                self.front = self.front.next
            else:
                prev = None
                curr = self.front
                count = 0
                while curr:
                    if count == ind:
                        break
                    count += 1
                    prev = curr
                    curr = curr.next
                if curr == None:
                    raise IndexError
                else:
                    prev.next = curr.next

    def copy_ll(self):
        if self.front == None:
            return None
        else:
            new_list = LinkedList()
            new_list.front = _Node(self.front.item)
            curr = self.front
            current_new = new_list.front
            while curr.next:
                new_node = _Node(curr.next.item)
                current_new.next = new_node
                curr = curr.next
                current_new = current_new.next
            return new_list

    def reverse(self):

        def reverse_help(l, node):
            if node.next == None:
                l.front = node
                return node
            else:
                reverse_help(l, node.next).next = node
                # Need to delete the previous next references for every node.
                node.next = None
                return node

        reverse_help(self, self.front)

    def filter_ll(self):
        if self == None:
            return None
        else:
            new_list = LinkedList()
            curr = self.front
            curr_new = None
            while curr:
                if curr.item % 2 == 0:
                    new_node = _Node(curr.item)
                    if new_list.front == None:
                        new_list.front = new_node
                        curr_new = new_list.front
                    else:
                        curr_new.next = new_node
                        curr_new = new_node
                curr = curr.next
            return new_list

    def count(self, item):
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        @type self: LinkedList
        @type item: object
        @rtype: int

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        if self.front == None:
            return 0
        else:
            curr = self.front
            count = 0
            while curr:
                if curr.item == item:
                    count += 1
                curr = curr.next
            return count

    def delete_item(self, item):
        """Remove the front occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.

        @type self: LinkedList
        @type item: object
        @rtype: None

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.delete_item(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.delete_item(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.delete_item(3)
        >>> str(lst)
        '[1]'
        >>> lst.delete_item(1)
        >>> str(lst)
        '[]'
        >>> lst.delete_item(1)
        >>> str(lst)
        '[]'
        """
        # NOTE: Implement without using any other LinkedList methods.
        curr = self.front
        prev = None

        while curr:
            if curr.item == item:
                break
            prev = curr
            curr = curr.next
        if curr == None:
            pass
        elif curr == self.front:
            self.front = curr.next
        else:
            prev.next = curr.next

    def map(self, f):
        """Return a new LinkedList whose nodes store items that are
        obtained by applying f to each item in this linked list.

        Does not change this linked list.

        @type self: LinkedList
        @type f: Function
        @rtype: None

        >>> func = str.upper
        >>> func('hi')
        'HI'
        >>> lst = LinkedList(['Hello', 'Goodbye'])
        >>> str(lst.map(func))
        '[HELLO -> GOODBYE]'
        >>> str(lst.map(len))
        '[5 -> 7]'
        """
        if self.front == None:
            return None
        else:
            new_list = LinkedList()
            new_list.front = _Node(f(self.front.item))
            curr = self.front
            curr_new = new_list.front
            while curr.next:
                new_node = _Node(f(curr.next.item))
                curr_new.next = new_node
                curr_new = curr_new.next
                curr = curr.next
            return new_list

    def __iter__(self):
        """Return a linked list iterator.

        Hint: the easiest way to implement __iter__ and __next__ is to
        make the linked list object responsible for its own iteration.

        In other words, __iter__(self) should simply return <self>.
        However, in order to make sure the loop always starts at the beginning
        of the list, you'll need a new private attribute for this class which
        keeps track of where in the list the iterator is currently at.

        @type self: LinkedList
        @rtype: LinkedList
        """
        self._iterator = self.front
        return self

    def __add__(self, L2):
        new_list = LinkedList()
        curr = self.front
        new_curr = None
        while curr:
            new_node = _Node(curr.item)
            if new_list.front == None:
                new_curr = new_node
                new_list.front = new_node
            else:
                new_curr.next = new_node
                new_curr = new_curr.next
            curr = curr.next

        curr = L2.front
        while curr:
            new_node = _Node(curr.item)
            if new_list.front == None:
                new_list.front = new_node
                new_curr = new_node
            else:
                new_curr.next = new_node
                new_curr = new_curr.next
            curr = curr.next
        return new_list

    def __next__(self):
        """Return the next item in the iteration.

        Raise StopIteration if there are no more items to return.

        Hint: If you have an attribute keeping track of the where the iteration
        is currently at in the list, it should be straight-forward to return
        the current item, and update the attribute to be the next node in
        the list.

        @type self: LinkedList
        @rtype: object

        >>> lst = LinkedList([1, 2, 3])
        >>> iter = lst.__iter__()
        >>> lst.__next__()
        1
        >>> lst.__next__()
        2
        >>> lst.__next__()
        3
        """
        ret = self._iterator
        if ret == None:
            raise StopIteration
        else:
            self._iterator = self._iterator.next
            return ret

    #    def insert_before(self, v1, v2):
    #        if self.front == None:
    #            pass
    #        else:
    #            prev = None
    #            curr = self.front
    #            while curr:
    #                if curr.item == v2:
    #                    break
    #                prev = curr
    #                curr = curr.next
    #            if curr == None:
    #                pass
    #            elif curr == self.front:
    #                new_node = _Node(v1)
    #                new_node.next = curr
    #                self.front = new_node
    #            else:
    #                new_node = _Node(v1)
    #                prev.next = new_node
    #                new_node.next = curr

    #    def delete_after(self, value):
    #        curr = self.front
    #        while curr:
    #            if curr.item == value:
    #                break
    #            curr = curr.next
    #        if curr == None or curr.next == None:
    #            pass
    #        else:
    #            curr.next = curr.next.next

    def del_front(self, value):
        if self.front == None:
            pass
        else:
            curr = self.front
            prev = None

            while curr and curr.next:
                if curr.item == value:
                    break
                prev = curr
                curr = curr.next
            if curr == self.front and curr.item == value:
                if curr.next:
                    curr.next.item += curr.item
                    self.front = curr.next
                else:
                    self.front = None
            elif curr != self.front and curr.item == value:
                if curr.next:
                    curr.next.item += curr.item
                    prev.next = curr.next
                else:
                    prev.next = None

    def insert_before(self, value, item):
        if self.front == None:
            pass
        else:
            curr = self.front
            prev = None
            while curr:
                if curr.item == value:
                    break
                prev = curr
                curr = curr.next
            if curr == None:
                pass
            else:
                if curr == self.front:
                    new_node = _Node(item)
                    new_node.next = self.front
                    self.front = new_node
                else:
                    new_node = _Node(item)
                    new_node.next = curr
                    prev.next = new_node

    def delete_after(self, value):
        if self.front == None:
            pass
        else:
            curr = self.front
            while curr:

                if curr.item == value:
                    break
                curr = curr.next
            if curr == None:
                pass
            else:
                if curr.next:
                    curr.next = curr.next.next

    def slice_out(self, j, k):
        """Remove the items in this list from positions <j> to <k-1> inclusive.
        Precondition: 0 < j <= k <= len(self)
        @type self: LinkedList
        @rtype: None
        >>> linky = LinkedList([0, 1, 2, 3, 4, 5, 6, 7])
        >>> str(linky)
        '[0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]'
        >>> linky.slice_out(2, 5)
        >>> str(linky)
        '[0 -> 1 -> 5 -> 6 -> 7]'
        """

        if self.front == None:
            pass
        elif self.front.next == None:
            pass
        else:
            curr = self.front
            j_1th, kth = None, None
            count = 0
            while curr:
                if count == j - 1:
                    j_1th = curr
                if count == k:
                    kth = curr
                count += 1
                curr = curr.next
            if j == k:
                kth = kth.next
            j_1th.next = kth
            self.size -= (k - j)

    def insert_duplicates(self, value):
        if self.front == None:
            pass
        else:
            curr = self.front
            while curr and curr.next:
                if curr.item == value:
                    new_node = _Node(value)
                    new_node.next = curr.next.next
                    curr.next = new_node
                    curr = new_node.next
                else:
                    curr = curr.next
            if curr == None:
                pass
            elif curr.item == value and curr.next == None:
                new_node = _Node(value)
                curr.next = new_node

    def swap(self, i, j):
        if self.front == None:
            pass
        else:
            ith, jth = None, None
            curr = self.front
            count = 0
            while curr:
                if count == i:
                    ith = curr
                if count == j:
                    jth = curr
                curr = curr.next
                count += 1
            if ith == None or jth == None:
                raise IndexError
            else:
                ith.item, jth.item = jth.item, ith.item

    def loop_check(self):
        if self.front == None:
            return False
        else:
            lst = []
            curr = self.front

            while curr:
                if curr in lst:
                    return True
                else:
                    lst.append(curr)
                    curr = curr.next
            if curr == None:
                return False

    def remove_front_double(self):
        if self.front == None:
            pass
        else:
            curr = self.front
            while curr and curr.next:
                if curr.item == curr.next.item:
                    break
                else:
                    curr = curr.next
            if curr.next:
                curr.next = curr.next.next

            else:
                pass

    def remove_front_satisfier(self, p):
        if self.front == None:
            pass
        else:
            curr = self.front
            prev = None
            while curr:
                if p(curr.item):
                    break
                else:
                    prev = curr
                    curr = curr.next
            if prev == None:
                self.front = self.front.next
                self.size -= 1
            else:
                if curr:
                    prev.next = curr.next
                    self.size -= 1
                else:
                    pass

    def insert_sorted(self, item):
        """Assuming list is sorted, insert item"""
        p = None
        c = self.front
        while c is not None and c.item < item:
            p = c
            c = c.next
        n = _Node(item)
        if p is None:
            n.next = c
            self.front = n
        elif c is None:
            p.next = n
        else:
            n.next = c
            p.next = n
        self.size += 1

    def insert_list(self, other, i) -> None:
        """insert a copy of LList other after position i into self."""

        if other.front is None:
            pass
        else:
            curr = other.front
            c_c = _Node(curr.item)
            o_copy_first = c_c
            curr = curr.next
            while curr is not None:
                new_node = _Node(curr.item)
                c_c.next = new_node
                c_c = c_c.next
                curr = curr.next
            c_s = self.front
            while i > 0:
                c_s = c_s.next
                i -= 1
            after = c_s.next
            c_s.next = o_copy_first
            c_c.next = after


def p(n):
    return n > 5


def reverse(node):
    print(node.item)
    if node.next == None:
        return node
    else:
        reverse(node.next).next = node
        node.next = None
        return node


def f(n):
    return n * 2


def remove_duplicates(lst: LinkedList) -> LinkedList:
    """fgfg"""
    h = lst.front
    c = lst.front
    while c is not None and c.next is not None:
        if c.item == c.next.item:
            c.next = c.next.next
        else:
            c = c.next
    return h


def shuffle_merge(head_1, head_2) -> _Node:
    """shufle merge two lists"""
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    # remove head_1 from list one and set it as the first elements of the new
    # list. Then set c1 to be second element of first list and c2 to be first
    # element of second list. This starts the merging easier.
    c = head_1
    h = head_1
    c1 = head_1.next
    c2 = head_2
    flag = True
    while c1 is not None and c2 is not None:
        if flag:
            new = c2
            c2 = c2.next
            c.next = new
            c = c.next
            flag = not flag
        else:
            new = c1
            c1 = c1.next
            c.next = new
            c = c.next
            flag = not flag
        print(c, c.next)
    if c2 is None and c1 is not None:
        c.next = c1
    if c1 is None and c2 is not None:
        c.next = c2
    return h


def equal(l_1: LinkedList, l_2: LinkedList) -> bool:
    """Return whether two linked lists L1 and L2 are equal."""
    c1 = l_1.front
    c2 = l_2.front
    while c1 is not None and c2 is not None:
        if c1.item != c2.item:
            return False
        c2 = c2.next
        c1 = c1.next
    return type(c1) == type(c2)


L = LinkedList()
L.add(0)
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
L.add(6)
L.add(7)
L.add(12)

L1 = LinkedList()
L1.add("a")
L1.add("b")
L1.add("c")
L1.add("d")
L1.add("e")


print(L)
L.insert_list(L1, 8)
print(L)


# L1 = LinkedList()
# L1.add(0)
# L1.add(1)
# L1.add(2)
# L1.add(3)
# L1.add(4)
# L1.add(5)
# L1.add(6)
# L1.add(7)
# print(L)
# print(L1)
# print(equal(L, L1))


# L2 = LinkedList()
# L2.add('D')
# L2.add('F')
# L2.add('L')
# print(L)
# print(L.size)
# print(L)
# L[-5] = 'A'
# print(L)


# L.delete_after(3)
# print(L)
# L.insert_before('A', 5)
# print(L)


# n1 = _Node(1)
# n2 = _Node(2)
# n3 = _Node(3)
# n4 = _Node(4)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# reverse(n1)
# print(n1.next.item)
# iter = L.__iter__()
# print(L._iterator)
# print(L.__next__())
# print(L.__next__())
# for el in L:
#    print(el.item)
