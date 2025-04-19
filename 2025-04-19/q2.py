# Q2. Develop a proof of correctness for binary search algorithm using Hoare Logic.

"""
Proof of Correctness for Binary Search using Hoare Logic

Problem:
Given a sorted list 'arr' and a target value 'x', find the index of 'x' in 'arr' using binary search.
Return -1 if 'x' is not present.

Precondition (P):
    arr is a list of elements sorted in non-decreasing order.
    x is the target element.

Postcondition (Q):
    If x is in arr, return index i such that arr[i] == x.
    If x is not in arr, return -1.

Binary Search Loop Invariant (I):
    x is in arr[l..r] if it is in arr at all.

Termination:
    The interval [l, r] reduces each iteration. When l > r, the loop stops.
"""


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(sorted_list, target)
    print(f"Index of {target}: {result}")
    target = 8
    result = binary_search(sorted_list, target)
    print(f"Index of {target}: {result}")
