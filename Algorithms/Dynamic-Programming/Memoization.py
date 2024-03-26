import math

def square_root(number):
    print('Long Time ...')
    return math.sqrt(number)

print('----------- Without Cache -----------------')
square = square_root(49)
print(square)
square = square_root(49)

def memoizied_square_root():
    cache = dict()
    def square_root(number):
        if number in cache:
            print('Long Time ...')
            return cache[number]
        else: 
            cache[number] = math.sqrt(number)
            return cache[number]
    return square_root
    
print('----------- With Cache -----------------')

square_root = memoizied_square_root()
square_cache = square_root(49)
print(square_cache)
square_cache = square_root(49)
