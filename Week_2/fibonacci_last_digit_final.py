# Uses python3
def get_fibonacci_last_digit_efficient(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i - 1] + fib[i - 2]) % 10)
    return fib[n]
    

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_efficient(n))
