def selection_sort(unsorted_list):
    length = len(unsorted_list)   
    if length <= 1:
        return
    for round in range(0, length - 1):
        smallest_item = unsorted_list[round]
        smallest_item_index = round
        for index in range(round, length - 1):
            if smallest_item <= unsorted_list[index + 1]:
                continue
            else: 
                smallest_item = unsorted_list[index + 1]
                smallest_item_index = index + 1
        tmp = unsorted_list[round]
        unsorted_list[round] = smallest_item
        unsorted_list[smallest_item_index] = tmp
    return unsorted_list


unsorted_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_list = selection_sort(unsorted_list)
print(sorted_list)