"Alireza Jafarpour 4012061009"
def Multi_Division(a , b , c):
    '''
    (int, int, int) -> boolean
    this function will for a given a, b, c, do the following:
Add a to itself b times.
Examples :
Multi_Division(42, 5, 10) ➞ False
Multi_Division(5, 2, 1) ➞ True
Multi_Division(1, 2, 3) ➞ False
	'''
    if (a * (2**b))%c ==0:
        return True
    else:
        return False
        
