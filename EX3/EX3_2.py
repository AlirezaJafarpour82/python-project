"Alireza Jafarpour 4012061009"
def Max_Adjacent_Product(list):
	'''
    (list)->int
    in the given a list of integers, this function finds the pair of adjacent elements that have the largest product and returns that product. 
Examples 
Max_Adjacent_Product( [3, 6, -2, -5, 7, 3] ) ➞ 2
Max_Adjacent_Product( [5, 6, -4, 2, 3, 2, -23] ) ➞ 30 
Max_Adjacent_Product( [0, -1, 1, 24, 1, -4, 8, 10] ) ➞ 80
	'''
	Product_List  = []
	for index in range( len(list) - 1):
		Product_Result = list[index] * list[index + 1]
		Product_List.append( Product_Result)
	Max_Product = Max( Product_List)

	return Max_Product
