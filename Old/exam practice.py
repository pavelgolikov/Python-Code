"""Some practice functions for the exam."""


def count_binary_string(s: str):
    """Return the number of 0s and ones in the string s"""
    if s == "":
        return (0, 0)
    else:
        prev = count_binary_string(s[1:])
        if s[0] == "0":
            return (prev[0] + 1, prev[1])
        else:
            return (prev[0], prev[1] + 1)


def palindrome(s: str) -> bool:
    """Return whether s is palyndrome"""
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        # return s[0] == s[-1] and palindrome(s[1:-1])
        if s[0] != s[-1]:
            return False
        return palindrome(s[1:-1])


def merge(s1: str, s2: str) -> str:
    """Return the string made by merging s1 and s2."""
    if len(s1) == 0 or len(s2) == 0:
        return s2 if len(s1) == 0 else s1
    else:
        if s1[0] < s2[0]:
            return s1[0] + merge(s1[1:], s2)
        else:
            return s2[0] + merge(s1, s2[1:])


def nested_sum(obj):
    """Return the sum of the numbers in a nested l i s t .
    Note that a nested l i s t is one of two things :
    1. a number
    2. a list of (smaller) nested l i s t s
    ©type obj: int I l i s t
    Srtype: int"""

    sum_ = 0
    if isinstance(obj, int):
        sum_ = sum_ + obj
    else:
        for lst_i in obj:
            sum_ += nested_sum(lst_i)
    return sum_


def freeze_list(lst) -> list:
    lst_ = []
    for el in lst:
        if not isinstance(el, list):
            lst_.append(el)
        else:
            lst_.append(freeze_list(el))
    return lst_
