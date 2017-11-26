import math


def merge(A, p, q, r):
    # p <= q < r
    L = A[p:q]
    L.append(float('inf'))
    R = A[q:r]
    R.append(float('inf'))
    i, j = 0, 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A


def merge_and_conquer_sort(A, p=None, r=None):
    assert isinstance(A, list)

    if p is None:
        p = 0
    if r is None:
        r = len(A)
    if p < r - 1:
        q = math.floor((p + r) / 2)
        A = merge_and_conquer_sort(A, p, q)
        A = merge_and_conquer_sort(A, q, r)
        A = merge(A, p, q, r)
    return A
