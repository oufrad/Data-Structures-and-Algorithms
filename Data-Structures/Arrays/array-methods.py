hunters = ['Kite', 'Knuckle', 'Killua', 'Ging', 'Hisoka', 'Gon']

'''
    Accessing an element: O(1)
    Searching for an element: O(n)
    Inserting an element: O(n)
    Deleting an element: O(n)
'''
hunters.append('Netero')  # O(1) -- it may be O(n) sometimes

hunters.pop()   # O(1)

hunters.insert(2, 'Biscuit')    # O(n)

hunters.remove(2)   # O(n)

hunters.index(4)    # O(n) : Searching

print(hunters)