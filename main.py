from sort import *
from plot import *
from file import *
from test import *


def main():
    number_of_words = list(range(1000, 11000, 1000))  # list of nubmer words to read from file

    Algorithm_time = {
        "Bubble sort": [[], []],  # for 0 time, for 1 sorted words
        "Selection sort": [[], []],
        "Insertion sort": [[], []],
        "Merge sort": [[], []],
    }

    for n in number_of_words:
        words = load_file("pan-tadeusz.txt", n)  # reading words from file
        print(f"Number of words:{n}")
        for key in Algorithm_time:
            if key == "Bubble sort":
                Algorithm_time[key][1], t = bubble_sort(words)  # for Bubble algorithm
            elif key == "Selection sort":
                Algorithm_time[key][1], t = selection_sort(words)  # for Selection algorithm
            elif key == "Insertion sort":
                Algorithm_time[key][1], t = insertion_sort(words)  # for Insertion algorithm
            elif key == "Merge sort":
                Algorithm_time[key][1] = words[:]  # because of recursive function we need copy before
                t = merge_sort(Algorithm_time[key][1])  # for Merge algorithm
            Algorithm_time[key][0].append(t)
            print(f"Time of execution in seconds for {key} algorithm:{t}")

    for key in Algorithm_time:
        make_plot(number_of_words, Algorithm_time[key][0], key)  # making individual plot
    one_plot(number_of_words, Algorithm_time)  # making one plot with every algorithm

    test(Algorithm_time, words)


if __name__ == "__main__":
    main()
