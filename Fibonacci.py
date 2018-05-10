from math import sqrt
def Fibonacci(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
