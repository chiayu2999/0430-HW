#Dynamic programming approach for fibonacci
memo = []
for i in range(101):
    memo.append(-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

import time
import matplotlib.pyplot as plt

# Measure execution time for Fibonacci function for n ranging from 10 to 100
n_values = range(10, 101, 10)
times = []

for n in n_values:
    start_time = time.time()
    fib(n)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times)
plt.xlabel('n')
plt.ylabel('Execution time (s)')
plt.title('Execution time of fib(n) using DP for n = 10, 20, ..., 100')
plt.show()