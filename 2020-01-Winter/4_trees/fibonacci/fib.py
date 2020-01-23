def fib(n):
    if n < 2: return 0
    if n == 2: return 1
    return fib(n - 1) + fib(n - 2)

def main():
    print('Testing for Nth term of Fibonacci sequence.')
    ans = fib(0)
    print('N = 0: ', ans)
    assert(ans == 0)
    ans = fib(5)
    print('N = 5: ', ans)
    assert(ans == 3)

if __name__=='__main__':
    main()
