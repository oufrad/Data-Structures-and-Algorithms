calculations_number = 0
def fibonacci_recursive(n):     # O(2^n) : Exponential Time Complexity
    global calculations_number
    calculations_number += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

fib_number = fibonacci_recursive(35)
print(f'Fibonacci Number : {fib_number}')
print(f'the number of calculations without Memoization is : {calculations_number}')

calcs_num_memoization = 0
def memoized_fibonacci():     # O(n) : Linear Time
    cache = dict()
    def fibonacci(number):
        global calcs_num_memoization
        calcs_num_memoization += 1
        if number <= 1:
            return number
        if number - 1 in cache and number - 2 in cache:
            return cache[number - 1] + cache[number - 2]
        else: 
            cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
            return cache[number]
    return fibonacci

fibonacci = memoized_fibonacci()

print('------------------')
fib_number = fibonacci(35)
print(f'Fibonacci Number : {fib_number}')
print(f'the number of calculations with Memoization is : {calcs_num_memoization}')
