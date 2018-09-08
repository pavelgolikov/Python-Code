"""Some recursion practice problems."""

import math

import random


dic = {'a': 1, 't':{'g': 5, 'l':{'r':{'q':2, 's':3}}}, 'b': 6}


def flatten_dic(dic):
    res = {}
    for k,v in dic.items():
        if not isinstance(v, dict):
            res[k] = v
        else:
            for i, j in flatten_dic(v).items():
                res[k+i] = j
    return res


print(flatten_dic(dic))



dic = {'a': 1, 'tg': 5, 'tlrq': 2, 'tlrs': 3, 'b': 6}


def unflatten_dic(dic):
   res = {}
   for k, v in dic.items():
       if len(k) == 1:
           res[k] = v
       else:
           inside_dic = {}
           outer_key = k[0]
           for i,j in dic.items():
               if i[0] == outer_key:
                   inside_dic[i[1:]] = j
           res[k[0]] = unflatten_dic(inside_dic)
   return res

print(unflatten_dic(dic))



'''CODING BAT PROBLEMS'''


st = 'this is a string'

def reverse(st):
   if len(st) == 1:
       return st
   else:
       return reverse(st[1:]) + st[0]

print(reverse(st))

def reverse_words(st):
   if len(st) == 0:
       return ''
   else:
       for i in range(len(st)):

           if st[i] == ' ':
               break
       if i == len(st)-1:
           return st + ' '
       else:
           return reverse_words(st[i+1:]) + st[0:i+1]


print(reverse_words(st))


def gcd(x,y):
   '''Uses Eucledian algorithm to recursively find the gcd of two numbers
   '''
   r=max([x,y])%min([x,y])
   if r == 0:
       return min([x,y])
   else:
       return gcd(min([x,y]), r)

print(gcd(7, 14))




def raise_neg(n, a):
   if a == -1:
       return 1/n
   else:
       return (1/n)*raise_neg(n, a+1)



print(raise_neg(3, -2))

w = 'leaf'


def elfish(w, dic = {}):
   '''Determines if a word is elfish'''
   if len(w) == 0:
       if len(dic) == 3:
           return True
       else:
           return False
   else:
       if w[0] == 'e' or w[0] == 'l' or w[0] == 'f':
           dic[w[0]] = 1
       return elfish(w[1:], dic)


print(elfish('fallen'))

x='parrotg'
w='rrosdcatsdtpg'

def x_ish(x, w):
   if len(x) == 0:
       return True
   else:
       flag = False
       for char in w:
           if char == x[0]:
               flag = True
       return flag and x_ish(x[1:], w)
print(x_ish(x,w))


def digits(n):

   if n < 10:
       return 1
   else:
       return 1 + digits(n//10)


print(digits(2310))

def maximum(lst):

   if len(lst) == 1:
       return lst[0]
   else:
       return max(lst[0],maximum(lst[1:]))

print(maximum([4,3,56,43,72,12]))


def triangle(n):
   if n == 0:
       return 0
   else:
       return n + triangle(n-1)

print(triangle(4))

def sum_digits(n):
   if n < 10:
       return n
   else:
       return (n%10) + sum_digits(n//10)

print(sum_digits(5279))

def digit_7(n):
   if n < 10:
       if n == 7:
           return 1
       else:
           return 0
   else:
       if n%10 == 7:
           return 1 + digit_7(n//10)
       else:
           return 0 + digit_7(n//10)

print(digit_7(65787320774))


def digit_8(n):
   if n < 10:
       if n == 8:
           return 1
       else:
           return 0
   else:
       if n%10 == 8 and (n//10)%10 == 8:
           return 4 + digit_8(n//10//10)
       elif n%10 == 8 and (n//10)%10 != 8:
           return 1 + digit_8(n//10)
       else:
           return 0 + digit_8(n//10)

print(digit_8(38888488))



def power_n(b,p):
   if p == 1:
       return b
   else:
       return b*power_n(b,p-1)

print(power_n(2,5))


def count_x(st):
   if len(st) == 0:
       return 0
   else:
       if st[-1] == 'x':
           return 1 + count_x(st[:-1])
       else:
           return 0 + count_x(st[:-1])

print(count_x('xjxfxuwkxxtoxxrjqwx'))


def count_hi(st):
   if len(st) == 0:
       return 0
   else:
       if st[-1] == 'i' and st[-2] == 'h':
           return 1 + count_hi(st[:-2])
       else:
           return 0 + count_hi(st[:-1])

print(count_hi('wfih42ehiwhid'))

def change_xy(st):
   if len(st) == 0:
       return ''
   else:
       if st[-1] == 'x':
           return change_xy(st[:-1]) + 'y'
       else:
           return change_xy(st[:-1]) + st[-1]

print(change_xy('fxgjeyfexxew'))


def change_pi(st):
   if len(st) == 0:
       return ''
   else:
       if st[-1] == 'i' and st[-2] == 'p':
           return change_pi(st[:-2])+'3.14'
       else:
           return change_pi(st[:-1]) + st[-1]

print(change_pi('fefppiifepiewpi'))



def no_x(st):
   if len(st) == 0:
       return ''
   else:
       if st[-1] == 'x':
           return no_x(st[:-1]) + ''
       else:
           return no_x(st[:-1]) + st[-1]

print(no_x('xyfxhfxx'))

def array_6(lst):
   if len(lst) == 0:
       return False
   else:
       if lst[-1] == 6:
           return True
       else:
           return False or array_6(lst[:-1])

print(array_6([4,5,6,7,32]))

def array_11(lst):
   if len(lst) == 0:
       return 0
   else:
       if lst[-1]==11:
           return 1 + array_11(lst[:-1])
       else:
           return 0 + array_11(lst[:-1])

print(array_11([1,2,3,11,4,5,3,11,87,6,4,]))


def array_220(lst):
   if len(lst) == 1:
       return False
   else:
       if lst[-2]*10 == lst[-1]:
           return True
       else:
           return False or array_220(lst[:-1])

print(array_220([2,20,4,5,7,8]))



def all_star(st):
   if len(st) == 1:
       return st[0]
   else:
       return all_star(st[:-1]) + '*' + st[-1]

print(all_star('hello'))


def pair_star(st):
   if len(st) == 1:
       return st[0]
   else:
       if st[-1] == st[-2]:
           return pair_star(st[:-1]) + '*' + st[-1]
       else:
           return pair_star(st[:-1]) + st[-1]

print(pair_star('rrrrrutyeeo'))


def end_x(st):
   if len(st) == 0:
       return ''
   else:
       if st[0] == 'x':
           return end_x(st[1:]) + st[0]
       else:
           return st[0] + end_x(st[1:])


print(end_x('xghsxfxxfrex'))


def count_pairs(st):
   if len(st) == 3:
       if st[0] == st[2]:
           return 1
       else:
           return 0
   else:
       if st[0] == st[2]:
           return 1 + count_pairs(st[1:])
       else:
           return 0 + count_pairs(st[1:])

print(count_pairs('xaxyuuha'))

def count_abc(s):
   if len(s) < 3:
       return 0
   elif len(s) == 3:
       if s[0] == 'a' and s[1] == 'b' and s[2]=='c':
           return 1
       else:
           return 0
   else:
       if s[0] == 'a' and s[1] == 'b' and (s[2]=='c' or s[2] == 'a'):
           return 1 + count_abc(s[1:])
       else:
           return 0 + count_abc(s[1:])

print(count_abc('abagkriabclgjabababc'))


def count_11(s):
   if len(s) == 1:
       return 0
   if len(s) == 2:
       if s == '11':
           return 1
       else:
           return 0
   else:
       if s[0:2] == '11':
           return 1 + count_11(s[2:])
       else:
           return 0 + count_11(s[1:])

print(count_11('gdst1f111gfd111'))


def string_clean(s):
   if len(s) == 1:
       return s
   else:
       if s[0] == s[1]:
           return string_clean(s[1:])
       else:
           return s[0] + string_clean(s[1:])

print(string_clean('thissgheiiisnnnne'))


def count_hi2(s):
   if len(s)==3:
       if s == 'xhi':
           return 0
       elif s[0:2] == 'hi' or s[1:3] == 'hi':
           return 1
   else:
       if s[0:3] == 'xhi':
           return 0 + count_hi2(s[3:])
       elif s[0:2] == 'hi':
           return 1 + count_hi2(s[2:])
       else:
           return 0 + count_hi2(s[1:])

print(count_hi2('xhihifgehhi'))

def paren_bit(s, flag = False):
   if len(s) == 0:
       return ''
   else:
       if s[0] == '(':
           return s[0] + paren_bit(s[1:], True)
       elif s[0] == ')':
           return s[0] + paren_bit(s[1:])
       else:
           if flag == True:
               return s[0] + paren_bit(s[1:], True)
           else:
               return paren_bit(s[1:])

print(paren_bit('fewf(sddsgd)tr(hwas)lidgsf3'))


def nest_paren(st):
   if len(st) == 0:
       return True
   else:
       if st[0] == '(' and st[-1] == ')':
           return True and nest_paren(st[1:-1])
       else:
           return False
print(nest_paren('(((())))'))

def string_count(s, sub_s):
   if len(s) < len(sub_s):
       return 0
   elif len(s) == len(sub_s):
       if s == sub_s:
           return 1
       else:
           return 0
   else:
       if s[0:len(sub_s)] == sub_s:
           return 1 + string_count(s[len(sub_s):], sub_s)
       else:
           return 0 + string_count(s[1:], sub_s)

print(string_count('catematocatfcat', 'at'))

def string_copies(s, sub_s, n):
   if n == 0:
       return True
   else:
       if len(s) < len(sub_s):
           return False
       else:
           if s[0:len(sub_s)] == sub_s:
               return string_copies(s[1:], sub_s, n-1)
           else:
               return string_copies(s[1:], sub_s, n)

print(string_copies("efjakakawdf", "aka", 1))


def string_dist(s, sub_s, flag = False):
   if len(s) < len(sub_s):
       return 0
   else:
       if s[0:len(sub_s)] == sub_s:
           return len(sub_s) + string_dist(s[len(sub_s):], sub_s, True)
       else:
           if flag == True:
               if s[len(s)-len(sub_s):] == sub_s:
                   return len(s)
               else:
                   return 0 + string_dist(s[:-1], sub_s, True)
           else:
               return 0 + string_dist(s[1:], sub_s, False)

print(string_dist("werscatcowwcatdfd", "cat"))




'''
HARDER RECURSIVE PROBLEMS
'''


def group_sum(l, n):
   if len(l) == 0:
       return False
   elif l[0] == n:
       return True
   elif l[0] > n:
       return group_sum(l[1:], n)
   else:
       return group_sum(l[1:], n-l[0]) or group_sum(l[1:], n)

print(group_sum([10,2,5,7], 25))


def group_sum6(l, n):
   if len(l) == 0:
       if n == 0:
           print('yes returning True')
           return True
       else:
           return False
   elif n == 0:
       #subtract iff l[0] == 6
       if l[0] == 6:
           return group_sum6(l[1:], n-6)
       else:
           print('yes got n==0')
           return group_sum6(l[1:], n)
   elif l[0] == n:
       return group_sum6(l[1:], n-l[0])
#    elif l[0] == n and l[0] == 6:
#        return True
   elif l[0] == 6:
       return group_sum6(l[1:], n-6)
   elif l[0] > n:
       return group_sum6(l[1:], n)
   else:
#        print(l[1:], n-l[0])
       return group_sum6(l[1:], n-l[0]) or group_sum6(l[1:], n)

print(group_sum6([5, 6, 2], 7))



def group_no_adj(l, n):
   if len(l) == 0:
       return False
   elif l[0] == n:
       return True
   elif l[0] > n:
       return group_no_adj(l[1:], n)
   elif len(l) == 1:
       return group_no_adj(l[1:], n-l[0]) or group_no_adj(l[1:], n)
   else:
       return group_no_adj(l[2:], n-l[0]) or group_no_adj(l[1:], n)

print(group_no_adj([10,2,5,1], 7))



def group_sum5(l, n):
   #if length is 0, return true if n was reached
   if len(l) == 0:
       if n == 0:
           print('yes returning True')
           return True
       else:
           return False
   elif n == 0:
       #keep going when n reaches 0 but subtract from n only if l[0] i divisible by 5
       if l[0] % 5 == 0:
           return group_sum5(l[1:], n-l[0])
       else:
           print('yes got n==0')
           return group_sum5(l[1:], n)
   #if l[0] is larger than n, skip it
   elif l[0] > n:
       return group_sum5(l[1:], n)
   elif l[0] == n:
       return group_sum5(l[1:], n-l[0])
   #if l[0] is divisible by 5, add it to sum
   elif l[0] % 5 == 0 and len(l) > 1:
       print(l)
       if l[1] == 1:
           return group_sum5(l[2:], n-l[0])
       else:
           return group_sum5(l[1:], n-l[0])
   elif l[0] % 5 == 0 and len(l) == 1:
       return group_sum5(l[1:], n-l[0])
   #consider both adding the next number to the sum and not adding
   else:
       return group_sum5(l[1:], n-l[0]) or group_sum5(l[1:], n)

print(group_sum5([10,1,20], 31))



def group_sum(l, n):
   if n == 0:
       return True
   elif len(l) == 0 or n < 0:
       return False
   elif l[0] > n:
       return group_sum(l[1:], n)
   else:
       #Insert a loop here that searches for similar elements immediately after
       i = 0
       while i < len(l):
           if l[0] == l[i]:
               i+=1
               continue
           else:
               break
       ind = min(i, len(l))
       #Compute how much we need to subtract from n
       tot = l[0]*ind
       return group_sum(l[ind:], n-tot) or group_sum(l[ind:], n)

print(group_sum([5,5,5,1,5,5], 10))


def counter(l,g1=0, g2=0):

       if len(l) == 0:
           if g1 == g2:
               return True
           else:
               return False
       else:
           g1_new = g1 + l[0]
           g2_new = g2 + l[0]
           return counter(l[1:], g1_new, g2) or counter(l[1:], g1, g2_new)

def split_array(l):
   return counter(l)

print(split_array([1,1,1,1]))

def counter(l,g1=0, g2=0):
   if len(l) == 0:
       if (g1%10 == 0 and g2%2 == 1) or (g2%10 == 0 and g1%2 == 1):
           return True
       else:
           return False
   else:
       g1_new = g1 + l[0]
       g2_new = g2 + l[0]
       return counter(l[1:], g1_new, g2) or counter(l[1:], g1, g2_new)

def split_odd10(l):
   return counter(l)

print(split_odd10([5,5,6,1]))

l = ['a', ['b', 'c', ['d', ['r'], 't']], 'x']

def flattener(l):
   lst = []
   for el in l:
       if isinstance(el, list):
           lst += flattener(el)
       else:
           lst.append(el)
   return lst


print(flattener(l))



def counter(l,g1=0, g2=0):
       if len(l) == 0:
           if g1 == g2:
               return True
           else:
               return False
       else:
           if l[0] % 5 == 0:
               g1_new = g1 + l[0]
               return counter(l[1:], g1_new, g2)
           elif l[0] % 3 == 0 and l[0] % 5 != 0:
               g2_new = g2 + l[0]
               return counter(l[1:], g1, g2_new)
           else:
               g1_new = g1 + l[0]
               g2_new = g2 + l[0]
               return counter(l[1:], g1_new, g2) or counter(l[1:], g1, g2_new)
def split_53(l):
   return counter(l)

print(split_53([5,5,3,3,3,1]))


'''HACKER RANK PROBLEMS'''


'''
formula for n'th row, r'th column: n!/(r! * (n-r)!)

The Pascal Triangle

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''


def pascal(n):

   if n == 0:
       return '1'
   else:
       s = ''
       for r in range(n+1):
           s+= str(int((math.factorial(n)/(math.factorial(r) * math.factorial(n-r))))) + ' '
       return pascal (n-1) +'\n' + s


print(pascal(4))



'''Convex Hull'''


l = [(1,2), (6,3), (3,9), (5,0), (2,15), (10,4), (8,10), (7,5)]

def is_left(p1, p2, p):
   '''Checks if point p lies to the left of the line from point p1 to point p2

   @type tuple: p1
   @type tuple: p2
   @type tuple: p
   rtype bool
   '''
   return (((p2[0] - p1[0])*(p[1] - p1[1])) - ((p[0] - p1[0])*(p2[1] - p1[1]))) > 0


def jarvis_hull(l):

   #Pick the right_most point in the list:
   right_most = l[0]
   for p in l:
       if p[0] > right_most[0]:
           right_most = p

   hull = []
   i = 0
   hull.append(right_most)
   while True:
       #keep track of latest point on the hull
       last_point_on_hull = hull[i]
       #find next point on the hull from the last point. iterate over all points in
       #l and find the one whose polar angle is largest
       #define endpoint initially to be the last_point_on_hull
       endpoint = l[0]
       #initiate a loop that will determine the next point on the hull
       for point in l:
           if endpoint == last_point_on_hull or is_left(last_point_on_hull, endpoint, point):
               endpoint = point
       if endpoint == hull[0]:
           break
       else:
           hull.append(endpoint)
           i+=1
   return hull

print(jarvis_hull(l))

def perimeter(l):
   total = 0
   for i in range(len(l)-1):
       total += math.sqrt((l[i+1][1] - l[i][1])**2 + (l[i+1][0] -l[i][0])**2)

   total += math.sqrt((l[0][1] - l[i+1][1])**2 + (l[0][0] -l[i+1][0])**2)
   return total


print(perimeter(jarvis_hull(l)))

'''Convex Hull with recursion'''

dic = {(1,2): 0, (6,3): 0, (3,9): 0, (5,0): 0, (2,15): 0, (10,4): 0, (8,10): 0, (7,5): 0}

#create a dictionary from a list of points like above

def is_left(p1, p2, p):
   '''Checks if point p lies to the left of the line from point p1 to point p2

   @type tuple: p1
   @type tuple: p2
   @type tuple: p
   rtype bool
   '''
   return (((p2[0] - p1[0])*(p[1] - p1[1])) - ((p[0] - p1[0])*(p2[1] - p1[1]))) > 0


'''Recursive Jarvis march with dictionary'''

def recursive_jarvis(dic, right_most, last_hull_point):
   if dic[right_most] == 'h':
       return dic
   else:
       endpoint = last_hull_point
       for point in dic.keys():
           if endpoint == last_hull_point or is_left(last_hull_point, endpoint, point):
               endpoint = point
       dic[endpoint] = 'h'
       return recursive_jarvis(dic, right_most, endpoint)


def jarvis_rec(dic):

#    Pick the right_most point in the list:
   right_most = random.choice(list(dic))
   for p in dic.keys():
       if p[0] > right_most[0]:
           right_most = p

   dic[right_most] = 1

   #start recursion
   return recursive_jarvis(dic, right_most, right_most)


print(jarvis_rec(dic))

'''Recursive Jarvis march with lists'''

#FINISH

st = 'rrrrfrfaaaaayjlllllldrwaaaaa'


def st_comp(st):

   if len(st)==1:
       return st[0]
   else:
       i = 0
       while True:
           if i+1 == len(st):
               return st[0] + str(i+1)
           if  st[i] == st[i+1]:
               i+=1
           else:
               break
       if i == 0:
           return st[0] + st_comp(st[i+1:])
       else:
           return st[0] + str(i+1) + st_comp(st[i+1:])

print(st_comp(st))


def st_comp_alt(A,B):
   if len(A) == 0 or len(B) == 0:
       return ['', A, B]
   res = ['', '', '']
   if A[0] == B[0]:
       res[0] += A[0]
       res_new = st_comp_alt(A[1:], B[1:])
       res[0]+= res_new[0]
       res[1]+= res_new[1]
       res[2]+= res_new[2]
   else:
       res[1] += A
       res[2] += B
   return res

print(st_comp_alt('abcdxyz', 'abcdtgj'))


def st_red(st, occured = []):
   if len(st) == 0:
       return ''
   else:
       if st[0] not in occured:
           occured += st[0]
           return st[0] + st_red(st[1:], occured)
       else:
           return st_red(st[1:], occured)


print(st_red('fabsabbaabbfbb'))



"""
def powers(n = number to analyze, k = number we are starting at, count):
   if number we are squaring is larger than n:
       return count
   elif we went too far and subtracted too much n < 0:
       return count
   elif n equals k**2:
       update count
       return count
   else:
       return how many times you reached n includng k plus not including k. Add
       thhese two numbers and return as count
"""


def powers(n,k, count = 0):
   if k >= n:
       return count
   elif n < 0:
       return count
   elif n == k**2:
       count+=1
       return count
   else:
       count += powers(n,k+1, count) + powers(n-(k**2), k+1, count)
       return count
print(powers(49,1))



l = [4, 5, 2, 5, 4, 3, 1, 3, 4]

def filtr(l, lst = []):
   if len(l) == 0:
       return lst
   else:
       if len(lst) == 0:
           lst.append([l[0],1])
       else:
           for el in lst:
               track = False
               if l[0] == el[0]:
                   el[1]+=1
                   track = True
                   break
           if track == False:
               lst.append([l[0],1])
       return filtr(l[1:], lst)



def filter_elements(l, k):
   st=''
   for el in filtr(l):
       print(el)
       if el[1] >=k:
           if len(st) == 0:
               st+=str(el[0])
           else:
               st+= ' '+ str(el[0])
   return st

print(filter_elements(l,2))
         
'''SUPER DIGITS'''

def super_digits(n):
   if n//10 == 0:
       return n
   else:
       st = str(n)
       l = []
       for i in range(len(st)):
           l.append(int(st[i]))
       summ = 0
       for el in l:
           summ += el

       return super_digits(summ)

print(super_digits(78))



#Sequences of colours.

def colours(st, by = 0, gr = 0):
   flag = True
   if len(st) == 0:
       return flag
   else:
       if st[0] == 'B':
           by += 1
       elif st[0] == 'G':
           gr += 1
       elif st[0] == 'Y':
           by -= 1
       elif st[0] == 'R':
           gr -= 1
       if abs(by) > 1 or abs(gr)> 1:
           flag = False
       return flag and colours(st[1:], by, gr)

print(colours('G'))


'''CONCAVE POLYGON'''

def list_converter(l):
    '''Converts list to dictionary of required foramt
    '''
    dic = {}
    for el in l:
        dic[el] = ''
    return dic

dic = {(4,2): '', (2,5): '', (8,8): '', (12,7): '', (15,4): '', (10,4): '', (11,1): ''}
l = [(4,2),(2,5),(8,8),(12,7),(15,4),(10,4),(11,1)]

def is_left(p1, p2, p):
    '''Checks if point p lies to the left of the line from point p1 to point p2
    
    @type tuple: p1
    @type tuple: p2
    @type tuple: p
    rtype bool
    '''
    return (((p2[0] - p1[0])*(p[1] - p1[1])) - ((p[0] - p1[0])*(p2[1] - p1[1]))) > 0
            
# def next_point_on_hull(l, point_on_hull, current_candidate):
#    '''Finds the next candidate from the list and current candidate
#    '''
#    for el in l:
#        if is_left(el, point_on_hull, current_candidate):
#            current_candidate = el
#    return current_candidate

def points_on_hull(dic, point_on_hull, current_candidate):
    '''Marks all points on the hull  in the dictionary
    '''
    for point in dic.keys():
        if current_candidate == point_on_hull or is_left(point_on_hull, current_candidate, point):
            current_candidate = point
    if dic[current_candidate] == 'h':
        return dic
    else:
        dic[current_candidate] = 'h'
        return points_on_hull(dic, current_candidate, current_candidate)


def concave(l):
    #convert list to dictionary of required format
    dic = list_converter(l)
    #pick left_most point
    left_most = random.choices(list(dic))[0]
    for p in dic.keys():
        if p[0] < left_most[0]:
            left_most = p
    points_on_hull(dic, left_most, left_most)
    flag = False
    for v in dic.values():
        if v != 'h':
            flag = True
    return flag

print(concave(l))
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            