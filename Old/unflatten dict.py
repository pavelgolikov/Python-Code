"""Scratch Flatten/Unflatten dict"""

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
