def bubble_sort(input_list):
    assert isinstance(input_list, list)

    len_list = len(input_list)
    for i in range(len_list - 1):
        for j in range(len_list - 1, i, -1):
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
    return input_list
