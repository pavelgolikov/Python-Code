import math


def sel_sort(lst):
    """
    Sorts a given list using Selection Sort.

    @param list lst: a list to be sorted
    rtype: list
    """
    # advance the index j through the entire array. Everything after j is
    # unsorted, everything before j is sorted.
    for j in range(len(lst)):
        # assume first unsorted element is the smallest, record its index
        index = j
        # iterate over all unsorted elements
        for i in range(j, len(lst)):
            # if we find an unsorted element smaller than lst[j], it becomes
            # the new smallest
            if lst[i] < lst[index]:
                # remember the index of the new smallest element
                index = i
        # swap new smallest element with element in position j
        lst[index], lst[j] = lst[j], lst[index]
    # return sorted list
    return lst


def ins_sort(lst):

    for i in range(len(lst)):
        el = lst[i]
        j = i-1
        while j >= 0 and el < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = el
    return lst


def sift_up(lst, ind):

    child = ind
    while child > 0:
        parent = math.floor((child-1)/2)
        if lst[child] > lst[parent]:
            lst[child], lst[parent] = lst[parent], lst[child]
            child = parent
        else:
            return


def heapify_up(lst):

    ind = 1

    while ind < len(lst):
        sift_up(lst, ind)
        ind += 1


def sift_down(lst, index, last):
    """
    Sifts down an element as far as it can down the heap
    @param list lst: heap to be repaired
    @param int index: index in the heap lst of the element that needs to
    @param int last: last index of lst
    be sifted down.
    rtype: none
    """
    # by default, we are swapping the root
    swap = index
    # math.floor((last-1)/2)
    
    while index < last:
        left_child = min(index*2 + 1, last)
        right_child = min(left_child + 1, last)
            
        # if element at left or right child is bigger than at the root,
        # we designate that element to be swapped
        
        if lst[swap] < lst[left_child]:
            swap = left_child
        if lst[swap] < lst[right_child]:
            swap = right_child
        # if the root is still designated to be swapped, break out of
        # the loop because we know that element at index and its children are
        # in heap order
        if swap == index:
            break
        # swap appropriate elements in lst
        lst[index], lst[swap] = lst[swap], lst[index]
        # reassign index to where the element from original index is now
        # and continue sifting it down.
        index = swap

   
def heapify_down(lst):
    """
    Makes lst into a max heap
    
    @param list lst: list to be made into a heap
    rtype: none
    """
    # we start at the parent of the last element of the heap and work our
    # way backwards to the first element at index 0.
    tracker = math.floor((len(lst)-2)/2)
    while tracker >= 0:
        sift_down(lst, tracker, len(lst)-1)
        tracker -= 1


def heap_sort(lst):
    """
    Sorts a given list lst using heap sort
    
    @param list lst: list to sort
    rtype list
    """
    # Make lst into a heap
    heapify_down(lst)
    # designate last element
    last = len(lst)-1
    
    # go through the whole list
    while last > 0:
        # swap last element with 0 element because largest element is in
        # 0 position.
        lst[0], lst[last] = lst[last], lst[0]
        # update last to exclude already sorted elements to the right
        last -= 1
        # restore the heap property of the lst by sifting down the element
        # in position 0 which is now not the largest.
        sift_down(lst, 0, last)
    return lst


def quick_sort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quick_sort(lst, lo, p-1)
        quick_sort(lst, p+1, hi)


def partition(lst, lo, hi):
    pivot = lst[hi]
    i = lo
    j = hi-1

    while True:
        while lst[i] < pivot and i < hi:
            i += 1
        while lst[j] > pivot and j > lo:
            j -= 1
        if i >= j:
            lst[hi], lst[i] = lst[i], lst[hi]
            return i
        if lst[j] < lst[i]:
            lst[j], lst[i] = lst[i], lst[j]


def find_nth(lst, lo, hi, k):
    """Find n'th largest number in list lst."""
    print(lo, hi, k)
    if lo < hi:
        p = partition(lst, lo, hi)
        print(p)
        if k < p:
            find_nth(lst, lo, p-1, k)
        elif k > p:
            find_nth(lst, p+1, hi, k)
        elif k == p:
            print(lst[p])
    elif lo == hi:
        print(lst[lo])
