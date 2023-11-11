#Piotr Niedziałek
import time

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