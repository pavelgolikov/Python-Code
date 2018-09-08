"""Random Recursive functions for practice"""

values_cache = {}


def fibbonacci(n: int) -> int:
    """
    Dynamic programming computation of fibbonaci sequence.
    """
    assert (isinstance(n, int)), 'Your input is not an integer'
    assert (n >= 0), 'You have entered an invalid input'

    # Check if value is in cache and return if it is:

    if n in values_cache:
        return values_cache[n]

    # Implement function itself

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        current_value = fibbonacci(n - 1) + fibbonacci(n - 2)
        values_cache[n] = current_value
        print(str(n) + ':' + str(current_value))
        return current_value


def summ(nlist: list) -> int:
    """
    Recursively sum the elements of the list.
    """
    if len(nlist) == 1:
        value = nlist[0]
        return value
    else:
        value = nlist[0] + summ(nlist[1:])
        return value


def rec_summ(olist) -> int:
    """
    Recursively sum the list of numbers.
    """

    total = 0
    for element in olist:
        if isinstance(element, list):
            total += rec_summ(element)
        else:
            total = total + element
    return total


def factorial(n: int) -> int:
    """
    Compute n factorial recursively.
    """
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def int_sum(n: int) -> int:
    """Recursively compute the sum of digits in n"""
    total = 0
    k = str(n)
    if len(k) == 1:
        return total + n
    else:
        return int_sum(int(k[0])) + int_sum(int(k[1:]))


def sum_pos_int(n: int, x: int) -> int:
    """Calculate the sum of the positive integers
    of n+(n-2)+(n-4)... (until n-x =< 0)."""

    print(n, ':', x)
    if n <= 0:
        return 0
    else:
        return n + sum_pos_int(n - x, x)


def harm_sum(n: int) -> float:
    """
    Calculate the harmonic sum of n-1.
    """
    if n == 1:
        return n
    else:
        return 1 / n + harm_sum(n - 1)


def geom_sum(n: int) -> float:
    """Recursively find the geometric sum of n."""
    if n == 0:
        return 1
    else:
        return (1 / 2) ** n + geom_sum(n - 1)


def max_value(nlist):
    """
    Return maximum value in the list.
    """
    if len(nlist) == 1:
        return nlist[0]
    else:
        return max(nlist[0], max_value(nlist[1:]))


def reverse(s: str) -> str:
    """
    Reverse s recursively.
    """

    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


def lcs(s1: str, s2: str) -> int:
    """
    Return the length of common subsequence of s1 and s2.
    """

    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[-1] == s2[-1]:
            return 1 + lcs(s1[:-1], s2[:-1])
        else:
            return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


def lcs_rec(s1: str, s2: str, d={}) -> int:
    """Return the length of common subsequence of s1 and s2. Recursive."""
    for k in d.keys():
        k1 = k.split()[0]
        k2 = k.split()[1]
        if (s1 == k1 and s2 == k2) or (s1 == k2 and s2 == k1):
            print(d)
            return d[k]
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[-1] == s2[-1]:
            value = 1 + lcs_rec(s1[:-1], s2[:-1], d)
            d[s1 + " " + s2] = value
            return value
        else:
            return max(lcs_rec(s1[:-1], s2, d), lcs_rec(s1, s2[:-1], d))


def lis(lst: list, list_=[]) -> list:
    """
    Return the longest increasing subsequence of sequence lst, as a list.
    """
    print(list_)
    if len(lst) == 0:
        return []
    else:
        if len(list_) == 0:
            list_.append(lst[0])
            lst += lis(lst[1:], list_)
        else:
            if lst[0] > list_[-1]:
                list_.append(lst[0])
                lst += lis(lst[1:], list_)
            else:
                lst += lis(lst[1:], list_)
    return list_


print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))


d = {"A": 1, "B": 2, "C": {"D": 5, "H": {"E": 8}}, "P": 3}


def flatten_dict(dic: dict) -> dict:
    """
    Flatten dictionary dic.
    """

    d = {}
    for k in dic.keys():
        if not isinstance(dic[k], dict):
            d[k] = dic[k]
        else:
            x = flatten_dict(dic[k])
            for key in x.keys():
                d[k + "." + key] = x[key]
    return d


print(flatten_dict(d))


def unflatten_dict(d1: dict) -> dict:
    """
    Unflatten dictionary d1
    """

    d = {}
    for k in d1.keys():
        if len(k) == 1:
            d[k] = d1[k]
        else:
            outer = k[0]
            if outer in d.keys():
                d[outer][k[2:]] = d1[k]
            else:
                d[outer] = {}
                d[outer][k[2:]] = d1[k]
    for key in d.keys():
        if not isinstance(d[key], dict):
            continue
        else:
            d[key] = unflatten_dict(d[key])
    return d


print(unflatten_dict({'A': 1, 'B': 2, 'C.D': 5, 'C.H.E': 8, 'P': 3}))
