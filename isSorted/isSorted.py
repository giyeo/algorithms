# Time Complexity: O(n)
# Proof: consider a sorted list L.
# For any index i in the list, it's possible to make the list no longer sorted by modifying only the element L[i]. So any algorithm that doesn't look at L[i] doesn't have enough information to guarantee that it will correctly decide whether the list is sorted or not.
# Since this holds for every index i, any correct algorithm must examine the entire list.

def isSorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def _test():
    test_cases = [
        [[1,2,3],   True],
        [[1,3,2],   False],
        [[],        True],
        [[1],       True]
    ]

    for i, test in enumerate(test_cases):
        assert isSorted(test[0]) == test[1]
    print("Done!")

if __name__ == '__main__':
    _test()
