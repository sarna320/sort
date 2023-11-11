#Piotr Niedziałek
def test(A, w):
    w_sorted = sorted(w)
    temp = True
    for key in A:
        if A[key][1] != w_sorted:  # checking if all algoithms sorted the same way
            print(
                f"Algorithm {key} sorted words not the same way as a built in function sorted(),therefore we can assume that it might not work correctly"
            )
            temp = False
    if temp == True:
        print(
            "All algorithms sorted words the same way as a built in function sorted(), therefore we can assume that they might work correctly"
        )