"Alireza Jafarpour 4012061009"
def Mile_Marathon(n):
    '''
    (int)->boolean
    '''
    a=0
    for i in n:
        if i < 0:
            i = -1 * i
        a=a+i
    if a == 25:
        return True
    else:
        return False
       
