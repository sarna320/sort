#Paweł Sarnacki
import matplotlib.pyplot as plt


def make_plot(n, t, name):
    ax = plt.subplots()[1]
    ax.plot(n, t)
    ax.set_xlabel("Number of words")
    ax.set_ylabel("Time of algorithm [s]")
    ax.set_title(name)
    plt.savefig("plots/" + (name.lower().replace(" ", "_")) + ".png")
    plt.show()

def one_plot(n,A):
    ax = plt.subplots()[1]
    for key in A:
        ax.plot(n,A[key][0],label=key)
    ax.set_xlabel("Number of words")
    ax.set_ylabel("Time of algorithm [s]")
    ax.legend()
    plt.savefig("plots/" + "plot" + ".png")
    plt.show()
