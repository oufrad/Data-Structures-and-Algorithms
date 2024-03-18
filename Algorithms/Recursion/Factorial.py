# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

def find_factorial_recursive(number, factorial = 1):    # O(n)
    if number == 1:     
        return factorial    # The Base Case
    factorial *= number
    number -= 1
    return find_factorial_recursive(number, factorial) # The Recursive Case

def find_factorial_iterative(number):   # O(n)
    factorial = 1
    for i in range(number, 0, -1):
        factorial = factorial * i
    return factorial

factorial = find_factorial_iterative(5)
print(f"Using The Interative Approach : {factorial}")

factorial = find_factorial_recursive(11)
print(f"Using The Recursive Approach : {factorial}")