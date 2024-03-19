def bubble_sort(unsorted_list):     # O(n^2) : Bubble sort may be the first one that comes to mind but it's not very effecient
    length = len(unsorted_list)
    if length <= 1:
        return
    for round in range(length - 1, 0, -1):  # O(n)
        for index in range(0, round):   # O(n)
            if unsorted_list[index] <= unsorted_list[index + 1]:
                continue
            else:
                tmp = unsorted_list[index + 1]
                unsorted_list[index + 1] = unsorted_list[index]
                unsorted_list[index] = tmp
    return unsorted_list

unsorted_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)