# Uses python3
def gcd_efficient(a, b):
	if b == 0:
		return a
	else:
		rem = a % b
		return gcd_efficient(b, rem)

def lcm_efficient(a, b):
	max_a = max(a, b)
	min_b = min(a, b)
	gcd_val = gcd_efficient(max_a, min_b)
	if gcd_val == 1:
		return (a * b)
	lcm = (a * b) // gcd_val
	return (int(lcm))

if __name__ == '__main__':
    inputs = input()
    a, b = map(int, inputs.split())
    print(lcm_efficient(a, b))

