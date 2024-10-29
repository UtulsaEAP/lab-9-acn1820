def fibonacci(n):
    fib = 0
    next_fib = 1
    for target in range(0,n):
        next_fib = fib + next_fib
        fib = next_fib - fib
    return fib

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')