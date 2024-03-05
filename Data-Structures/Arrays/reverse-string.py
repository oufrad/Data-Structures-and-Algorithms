greeting = "Hi My name is mohamed oufrad !"

def reverse_string(forword):
    if forword is None or len(forword) < 2 or type(forword) != str:     # O(1)
        return False
    backword = [] # O(1)
    length = len(forword)   # O(1)
    for i in range(length - 1, -1, -1):   # O(n)
        backword.append(forword[i])   # O(1) Sometimes O(n)
    return ''.join(backword)   # O(n)

greeting_backwords = reverse_string(greeting)   # O(n + n + 3) = O(2n + 3) = O(n)

print(greeting_backwords)