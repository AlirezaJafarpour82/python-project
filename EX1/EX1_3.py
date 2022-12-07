"Alireza Jafarpour 4012061009
def ThirdEdge(FirstEdge,secondEdge) :
    '''
    (int,int) -> int
    In this function we will calculate the maximum ThirdEdge of an triangle by having its FirstEdge and secondEdge.

    Examples : 
    ThirdEdge(8, 10) ➞ 17  
    ThirdEdge(5, 7) ➞ 11 
    ThirdEdge(9, 2) ➞ 10
    '''
    if FirstEdge>0 and secondEdge>0 :
        ThirdEdge = ( FirstEdge + secondEdge ) -1
    else :
        print('it is impossible')
        
    return ThirdEdge
print(ThirdEdge(-1,4))
