# Uses python3
# Uses Stress Testing to check efficiency and correctness between naive and efficient algorithm.
import random
def calc_fib(n):
	fib = [0, 1]
	for i in range(2, n+1):
		fib.append(fib[i - 1] + fib[i - 2])
	return fib[n]

def rec_fib(n):
	if n <= 1:
		return n
	return rec_fib(n - 1) + rec_fib(n - 2)


while(True):
	n = random.randint(1, 46)
	print("***************************************")
	print(n)
	rec_output = rec_fib(n)
	calc_output = calc_fib(n)
	if(rec_output == calc_output):
		print(rec_output)
		print(calc_output)
		print("OK")
	else:
		print(rec_output)
		print(calc_output)
		print("INCORRECT OUTPUT")
		break
	print("*****************************************")

