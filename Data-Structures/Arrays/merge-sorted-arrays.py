# Merge Two sorted arrays into One bigger sorted Array
from time import time

def merge_sorted_arrays(arr_1, arr_2):
    arr_1_lenght = len(arr_1)
    arr_2_lenght = len(arr_2)

    merged_array = [0] * (arr_1_lenght + arr_2_lenght)

    i = j = k = 0

    while i < arr_1_lenght and j < arr_2_lenght:
        if arr_1[i] < arr_2[j]:
            merged_array[k] = arr_1[i]
            i += 1
        else:
            merged_array[k] = arr_2[j]
            j += 1
        k += 1

    while i < arr_1_lenght:
        merged_array[k] = arr_1[i]
        i += 1
        k += 1

    while j < arr_2_lenght:
        merged_array[k] = arr_2[j]
        j += 1
        k += 1

    return merged_array

marged_array = merge_sorted_arrays([0,3,4,31], [4,6,30])