
word = 'bard'

olist = ['ard', 'adr', 'rad', 'rda', 'dra', 'dar']

letter = 'b'


def permuter(olist, letter):
    newlist = []
    for i in range(len(olist)):
        for j in range(len(olist[i])+1):
            print(olist[i][:j] + letter + olist[i][j:])
            newlist = newlist + [olist[i][:j] + letter + olist[i][j:]]
    return newlist


def get_permutations(string):
    if len(string) == 1:
        return string
    else:
        permuted = permuter(get_permutations(string[1:]), string[0])
        return permuted
