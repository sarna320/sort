import time
import matplotlib.pyplot as plt


def bubble_sort(list):
    sorted_list = list[:]  # copy of original list, so it is not modified
    n = len(sorted_list)
    start = time.process_time()
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
    return 0, 0


def selection_sort(list):
    return 0, 0


def merge_pass(list):
    return 0, 0


def load_file(path, n):
    with open(
        path, "r", encoding="utf8"
    ) as file:  # opening file from your working folder
        data = file.read()
    list_of_words = data.split(maxsplit=n)
    list_of_words.pop()
    return list_of_words


def make_plot(n, t, name):
    ax = plt.subplots()[1]
    ax.plot(n, t)
    ax.set_xlabel("Number of words")
    ax.set_ylabel("Time of algorithm [s]")
    ax.set_title(name)
    plt.savefig("plots/" + (name.lower().replace(" ", "_")) + ".png")
    plt.show()


def main():
    number_of_words = list(range(1000, 5000, 1000))

    Algorithm_time = {
        "Bubble sort": [],
        "Selection sort": [],
        "Insertion sort": [],
        "Merge sort": [],
    }

    for n in number_of_words:
        words = load_file("pan-tadeusz.txt", n)
        words_bubble, t = bubble_sort(words)
        Algorithm_time["Bubble sort"].append(t)
        print("Czas wykonania w sekundach Bubble sort:", t)

        words_selection, t = selection_sort(words)  # for Selection algorithm
        Algorithm_time["Selection sort"].append(t)
        print("Czas wykonania w sekundach Selection sort:", t)

        words_insertion, t = insertion_sort(words)  # for Insertion algorithm
        Algorithm_time["Insertion sort"].append(t)
        print("Czas wykonania w sekundach Insertion sort:", t)

        words_merge, t = merge_pass(words)  # for Merge algorithm
        Algorithm_time["Merge sort"].append(t)
        print("Czas wykonania w sekundach Merge sort:", t)

    for key in Algorithm_time:
        make_plot(number_of_words, Algorithm_time[key], key)

    if words_bubble == words_insertion == words_merge == words_selection:
        print("All algorithms sorted words the same way, therefore they work correctly")
    else:
        print(
            "Not all algorithms sorted words the same way, therefore they might not work correctly"
        )


main()
