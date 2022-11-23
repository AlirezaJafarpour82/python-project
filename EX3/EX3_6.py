"Alireza Jafarpour 4012061009"
def Face_Interval(a):
    '''
    (int)->str
    In mathematics, interval is the difference between the largest number and the smallest number
in a list.
this function takes a list and returns ":)" if the interval of the list is equal to any other
element; otherwise returns “:(".
'''
    if len(a)==0:
        return (':/')
    a.sort()
    b = a[len(a)-1] - a[0]
    if i.count(b) == 1:
        return ":)"
    else:
        return ":("
