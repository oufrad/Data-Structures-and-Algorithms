def merge_sort(unsorted_list):
    length = len(unsorted_list)

    if length <= 1:
        return unsorted_list
    
    mid = length // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    if left is None and right is None:
        return 
    merged_array = []
    left_index, right_index = 0,0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1

        else:
            merged_array.append(right[right_index])
            right_index += 1
    merged_array.extend(left[left_index:])
    merged_array.extend(right[right_index:])

    return merged_array


unsorted_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)