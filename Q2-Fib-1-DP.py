import time
#Dynamic programming approach for fibonacci
def fib_dp(n):
    memo = []
    for i in range(n+1):
        memo.append(-1)

    memo[0] = 0
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

# Find the maximum value of n for which fib_dp(n+1) does not cause the computer to crash
# Measure execution time for Fibonacci function for n ranging from 10 to 10000
n_values = range(10, 10001, 10)
times = []

for n in n_values: 
    start_time = time.time()
    fib_dp(n+1)
    end_time = time.time()
    times.append(end_time - start_time)

# Determine the maximum value of n for which execution time is less than 1 second
threshold = 1
max_n = -1
for i in range(len(times)):
    if times[i] > threshold:
        break
    max_n = n_values[i]

print("Maximum value of n for DP approach: ", max_n)