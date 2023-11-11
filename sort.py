import time


def bubble_sort(list):
    sorted_list = list[:]  # copy of original list, so it is not modified
    start = time.process_time()
    n = len(sorted_list)
    for i in range(n):
        change = False
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )
                change = True
        if not change:
            break
    stop = time.process_time()
    return sorted_list, stop - start


def insertion_sort(list):
    sorted_list = list[:]
    start = time.process_time()
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
    stop = time.process_time()
    return sorted_list, stop - start


def selection_sort(list):
    sorted_list = list[:]
    start = time.process_time()
    n = len(sorted_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    stop = time.process_time()
    return sorted_list, stop - start


def merge_sort(list):
    
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1

