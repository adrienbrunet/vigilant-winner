def insertion_sort(unordered_list):
    assert isinstance(unordered_list, list)

    for j in range(1, len(unordered_list)):
        # insert element into the sorted sequence list[1..j-1]
        key = unordered_list[j]
        i = j - 1
        while i >= 0 and unordered_list[i] > key:
            unordered_list[i + 1] = unordered_list[i]
            i -= 1
        unordered_list[i + 1] = key
    return unordered_list
