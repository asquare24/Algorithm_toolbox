# Uses python3
def fibonacci_sum_efficient(n):
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
    for i in range(period):
        print(i, fib_mod[i])

    sum_fib = fib_mod[(n + 2) % period] - 1
    if sum_fib == -1: # It takes two numbers to find a sum. So, sum of n fib nos  + 1 = (n+2)th fibo number. Therefore, for n+2th no to be zero, sum of n fibos must be 9.
        return 9
    return sum_fib

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_efficient(n))
