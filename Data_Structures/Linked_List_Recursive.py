"""Recursive linked list class."""


class LinkedListRec:
    """Recursive Linked List"""

    def __init__(self, items):
        """ (LinkedListRec, list) -> NoneType

        Create a new linked list containing the elements in items.
        If items is empty, self.first initialized to EmptyValue.
        """
        if len(items) == 0:
            self.first = None
            self.rest = None
        else:
            self.first = items[0]
            self.rest = LinkedListRec(items[1:])




    def __str__(self):
        if self.first == None:
            return ''
        else:
            s = str(self.first) + "->"
            s += self.rest.__str__()
            return s

    def size(self):
        """Return the size of the list

        @:param self LinkedListRecu: this recursive linked list
        @:rtype None
        """

        if self.first == None:
            return 0
        else:
            count = 1
            count += self.rest.size()
            return count

    def find_6(self):
        """Find how many times 6 occurs in the list.

        @:param self LinkedListRec: this list
        @:rtype int: number of times 6 occurs in the list
        """

        if self.first == None:
            return 0
        else:
            count = 0
            if self.first == 0:
                count += 1
            count += self.rest.find_6()
            return count

    def find_num_times(self, item):
        if self.first == None:
            return 0
        else:
            count = 0
            if self.first == item:
                count += 1
            count += self.rest.find_num_times(item)
            return count

    def find_sum(self):
        if self.first == None:
            return 0
        else:
            list_sum = self.first
            list_sum += self.rest.find_sum()
            return list_sum



    def remove_first(self):
        """Remove the first element of the list

        @:param self LinkedListRec: this list
        @:rtype None
        """
        if self.first == None:
            pass
        else:
            # print(self.rest)
            self.first = self.rest.first
            self.rest.remove_first()


    def remove_ith(self, i):
        """Remove i'th item from the list.

        Precondition: 1 < i < self.size()

        @:param self LinkedListRec: this list
        @:param i int: number of item to be removed
        @:rtype None
        """
        print(self.first)
        if self.first == None:
            pass
        else:
            if i > 1:
                self.rest = self.rest.remove_ith(i - 1)
            else:
                self = self.rest
            return self

    def remove_even(self):
        if self.first == None:
            pass
        else:
            if self.first % 2 == 0:
                self = self.rest.remove_even()
            else:
                self.rest = self.rest.remove_even()
            return self

    def insert_at_front(self, item):

        if self.first == None:
            self.first = item
            self.rest = LinkedListRec([])
        else:
            self.rest.insert_at_front(self.first)
            self.first = item


    def insert_at_back(self, item):
        if self.first == None:
            self.first = item
            self.rest = LinkedListRec([])
        else:
            self.rest.insert_at_back(item)


    def insert_at_ith(self, i, item):
        if self.first == None:
            self.first = item
            self.rest = LinkedListRec([])
        else:
            if i == 0:
                self.rest.insert_at_ith(i, self.first)
                self.first = item
            else:
                self.rest.insert_at_ith(i-1, item)


    def rep_items_help(self, obj: object) -> bool:
        """Return if obj appears anywhere in the list"""
        if self.first == None:
            return False
        else:
            flag = False
            if self.first == obj:
                return True
            else:
                flag = flag or self.rest.rep_items_help(obj)
            return flag

    def rep_item(self) -> bool:
        """Return True if there are repeated items in the list"""
        if self.first == None:
            return False
        else:
            flag = self.rest.rep_items_help(self.first)
            if flag:
                return True
            else:
                flag = flag or self.rest.rep_item()
            return flag


    def count_even(self) -> int:
        """Return the number of even items in the list"""
        if self.first == None:
            return 0
        else:
            count = 0
            if self.first % 2 == 0:
                count += 1
            count += self.rest.count_even()
            return count

llr = LinkedListRec([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(llr)
print(llr.count_even())
# print(llr)