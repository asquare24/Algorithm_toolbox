# Uses python3
def get_fibonacci_huge_efficient(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    period = 0 # After period, move two numbers ahead to check if numbers start from 0 and 1
    fib_mod = [0, 1]
    i = 2

    while(True):
        previous, current = current, previous + current
        period = period + 1
        fib_mod.append(current % m)
        if fib_mod[i-1] == 0 and fib_mod[i] == 1:
            break
        i = i + 1
    rem = n % period
    return fib_mod[rem]

if __name__ == '__main__':
    inputs = input();
    n, m = map(int, inputs.split())
    print(get_fibonacci_huge_efficient(n, m))
