from ..isSorted.isSorted import isSorted

def binarySearch(array, target):
    
    # if(isSorted(array) == False):
    #     return -2
    lenght = len(array)
    if(lenght == 0):
        return -1

    (left, right) = (0, lenght - 1)
    while left <= right:
        mid = (left + right) // 2

        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

def _test():
    test_cases = [
        [([1,2,3],  2),  1],
        [([1,2,3],  1),  0],
        [([1,2,3],  3),  2],
        [([],       2),  -1],
        [([1],      1),  0]
    ]

    for i, test in enumerate(test_cases):
        assert binarySearch(*test[0]) == test[1]
    print("Done!")

if __name__ == '__main__':
    _test()