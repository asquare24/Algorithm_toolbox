# Uses python3
def fibonacci_sum_squares_efficient(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    period = 0 # After period move two numbers ahead to check if numbers start from 0 and 1
    fib_mod = [0, 1]
    i = 2

    while(True):
        previous, current = current, (previous + current)
        period = period + 1
        fib_mod.append(current % 10)
        if fib_mod[i-1] == 0 and fib_mod[i] == 1:
            break
        i = i + 1

    ans = fib_mod[n % period] * fib_mod[(n + 1) % period]
    return ans % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_efficient(n))
