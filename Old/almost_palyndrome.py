"""Palyndrome"""

s = 'rsaptar'


def is_palyndrome(s):
    """Determines if s is palyndrome"""
    flag = True
    half = len(s)//2
    for i in range(half):
        if s[i] != s[len(s)-1-i]:
            flag = False
    return flag


def a_p_helper(s, index=0):
    """Helper function for almost palyndrome"""
    flag = False
    if is_palyndrome(s) is True:
        return True
    else:
        if index > len(s)-2:
            return False
        else:
            # do not switch current index
            # flag = flag or a_p_helper(s, index + 1)
            # switch current index
            switched = s[:index] + s[index+1] + s[index] + s[index+2:]
            # flag = flag or a_p_helper(switched, index + 2)
            return a_p_helper(switched, index + 2) or a_p_helper(s, index + 1)


print(a_p_helper(s))


def almost_palyndrome(s):
    """Almost Palyndrome"""
    return a_p_helper(s)
