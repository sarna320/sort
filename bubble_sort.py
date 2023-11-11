#Piotr Niedziałek
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