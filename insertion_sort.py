#Paweł Sarnacki
import time

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