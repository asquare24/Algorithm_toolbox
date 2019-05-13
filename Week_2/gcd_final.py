# Uses python3
def gcd_efficient(a, b):
    if b == 0:
    	print(a)
    	return
    a_prime = a % b
    gcd_efficient(b, a_prime)


inputs = input()
a, b = map(int, inputs.split())
max_a = max(a, b)
min_b = min(a, b)
gcd_efficient(max_a, min_b)