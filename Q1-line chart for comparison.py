import time
import matplotlib.pyplot as plt

# Fibonacci_recursive
def fibonacci_rec(n):
    if n in [1,2]:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Measure execution time for Fibonacci_recursive function for n ranging from 10 to 100
n_values = range(10, 101, 10)
times_rec = []

for n in n_values:
    start_time = time.time()
    fibonacci_rec(n)
    end_time = time.time()
    times_rec.append(end_time - start_time)

# Dynamic programming approach for fibonacci
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

# Measure execution time for fib function for n ranging from 10 to 100
times_dp = []

for n in n_values:
    start_time = time.time()
    fib(n)
    end_time = time.time()
    times_dp.append(end_time - start_time)

# Plot the results as a line chart
plt.plot(n_values, times_rec, label='Fibonacci_recursive')
plt.plot(n_values, times_dp, label='DP')
plt.xlabel('n')
plt.ylabel('Execution time (s)')
plt.title('Execution time of Fibonacci_recursive and DP for n = 10, 20, ..., 100')
plt.legend()
plt.show()
