# Fibonacci_recursive implementation
def fib_rec(n):
    if n in [0, 1]:
        return n
    return fib_rec(n-1) + fib_rec(n-2)
#use binary search, range from 0 to 10,000
def find_max_n():
    low, high = 0, 10000
    max_n = 0
    while low <= high:
        mid = (low + high) // 2
        try:
            fib_rec(mid + 1)
            max_n = mid
            low = mid + 1
        except RecursionError:
            high = mid - 1
    return max_n

max_n = find_max_n()
print("The maximum value of n such that computing F(n+1) recursively does not cause a stack overflow error is:", max_n)