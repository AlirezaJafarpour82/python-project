"Alireza Jafarpour 4012061009"
def Face_Interval(num):
    """
    ([int]) -> str
    in the given a list of integers, this function finds the pair of adjacent elements that have the largest product and
returns that product.
Examples :
Face_Interval( [3, 6, -2, -5, 7, 3] ) ➞ 21
Face_Interval( [5, 6, -4, 2, 3, 2, -23] ) ➞ 30
Face_Interval( [0, -1, 1, 24, 1, -4, 8, 10] ) ➞ 80
    ""
    a = []
    
    for i in range(0 , len(num)-1):
        b = num[i] * num[i+1]
        a.append(b)
    a.sort(reverse=True)
    return a[0]
 
