def insertion_sort(unsorted_list):  # O(n^2) But O(n) when you have almost sorted list or you have a small list
    length = len(unsorted_list)
    if length <= 1:
        return
    for round in range(1, length):
        key = unsorted_list[round]
        index = round - 1
        while index >= 0 and key < unsorted_list[index]:
            unsorted_list[index + 1] = unsorted_list[index]
            index -= 1
        unsorted_list[index + 1] = key
    return unsorted_list

unsorted_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_list = insertion_sort(unsorted_list)
print(sorted_list)