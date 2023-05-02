# Fibonacci_recursive
def fibonacci_rec(n):
    if n in [1,2]:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

import time
import matplotlib.pyplot as plt

# Measure execution time for Fibonacci function for n ranging from 10 to 100
n_values = range(10, 101, 10)
times = []

for n in n_values:
    start_time = time.time()
    fibonacci_rec(n)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times)
plt.xlabel('n')
plt.ylabel('Execution time (s)')
plt.title('Execution time of fibonacci_rec(n) for n = 10, 20, ..., 100')
plt.show()