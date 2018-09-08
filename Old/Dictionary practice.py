"""Some functions to practice with lists and dictionaries."""


def count_lists(list_):
    """Count the number of lists in a possibly nested list list_."""
    if not isinstance(list_, list):
        result = 0
    else:
        result = 1
        for i in list_:
            print(i)
            result = result + (count_lists(i))
    return result


def flatten_list(a, result=None):
    """Flattens a nested list.

       >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
       [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result


def flatten_dictionary(dic, key = '', result = None):
    """Flatten dictionary dic."""
    if result is None:
        result = {}
    for x, y in dic.items():
        if isinstance(y, dict):
            flatten_dictionary(y, str(key)+str(x)+'.', result)
        else:
            result[str(key)+str(x)] = y

    return result


def contains_satisfier(list_):
    """Check if a possibly nested list contains satisfier."""
    res = False
    if not isinstance(list_, list):
        res = list_ > 5
    else:
        for el in list_:
            res = res or contains_satisfier(el)
    return res


def tree_reverse(lst):
    lst.reverse()
    list_ = []
    for el in lst:
        if isinstance(el, list):
            list_ += [tree_reverse(el)]
        else:
            list_.append(el)
    return list_
