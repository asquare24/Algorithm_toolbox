# Uses python3
def fibonacci_partial_sum_efficient(m, n):
    if n <= 1:
        return n


    previous = 0
    current  = 1
    period = 0 # After period move two numbers ahead to check if numbers start from 0 and 1
    fib_mod = [0, 1]
    i = 2

    while(True):
        previous, current = current, previous + current
        period = period + 1
        fib_mod.append(current % 10)
        if fib_mod[i-1] == 0 and fib_mod[i] == 1:
            break
        i = i + 1

    sum_fib_m = fib_mod[(m + 1) % period] - 1 # Finding the aum of m-1 fibonacci numbers.
    sum_fib_n = fib_mod[(n + 2) % period] - 1
    diff = sum_fib_n - sum_fib_m
    if diff < 0:
        return diff + 10
    else:
        return diff

if __name__ == '__main__':
    inputs = input();
    m, n = map(int, inputs.split())
    print(fibonacci_partial_sum_efficient(m, n))