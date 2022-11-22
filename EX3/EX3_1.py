"Alireza Jafarpour 4012061009"
def Collatz_Conjecture(num):
	"""
    (int) -> int
    this function helps us to ubderstand how many times it takes to reach number one in order to following caculations.
Collatz_Conjecture (2) ➞ 1
Collatz_Conjecture(3) ➞ 7
Collatz_Conjecture(10) ➞ 6
    """
	step = 0

	if num > 0:
		while num != 1:
			if num % 2 == 0:
				num /= 2
			else:
				num *= 3
				num += 1
			step += 1
	else:
		return "Your number is invalid"
	return step
