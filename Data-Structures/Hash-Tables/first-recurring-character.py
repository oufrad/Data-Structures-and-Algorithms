# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return None

def find_first_recurring_char(input_array):
    occured_numbers = {}
    for element in input_array:     # O(n)
        if element in occured_numbers:      # O(1)  : searching element in Hash Table (most of the time)
            return element
        else:
            occured_numbers[element] = True     # O(n)  : pushing an element in hash table 
    return None


input_array = [2,1,1,2,3,5,1,2,4]
first_recurring_char = find_first_recurring_char(input_array)
print(first_recurring_char)