# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

def fibonacci_iterative(n):     # O(n)
    previous = 1
    pre_previous = 0
    fibonacci_number = 0
    if n == 1:
        return 1
    for i in range(1, n):
        fibonacci_number = pre_previous + previous
        pre_previous = previous
        previous = fibonacci_number
    return fibonacci_number

def fibonacci_recursive(n):     # O(2^n) : Exponential Time Complexity (altough it's more readable it's not an ideal solution)
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

index_fibonacci = fibonacci_iterative(40)
print(f"Using The Interative Approach : {index_fibonacci}")

index_fibonacci = fibonacci_iterative(40)
print(f"Using The Recursive Approach : {index_fibonacci}")