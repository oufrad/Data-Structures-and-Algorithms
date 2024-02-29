hunters = ['Kite', 'Knuckle', 'Killua', 'Ging', 'Hisoka', 'Gon']

# Linear Time O(n)
def findGing(hunters):
    for hunter in hunters:
        if hunter == 'Ging':
            print("we Found Ging !")

findGing(hunters)

# Constant Time O(1)
def findFirstHunter(hunters):
    print(hunters[0])

findFirstHunter(hunters)

# Quadratic Time O(n^2)
def print_all_pairs(hunters):
    for hunter in hunters:
        print('------------------')
        for next_hunter in hunters:
            print(hunter, next_hunter)
        print('------------------')

print_all_pairs(hunters)

# Fun Challenge
def funChallenge(input): 
    a = 10      # O(1)
    a = 50 + 3      # O(1)  
    for e in input:     # O(n)
        stranger = True     # O(n)
        a = a + 1       # O(n)
    return a    # O(1)

# O(n + n + n + 3) = O(3 + 3n) = O(n)