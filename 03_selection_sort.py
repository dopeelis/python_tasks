arr = [0, 3, 24, 2, 3, 7]


def selection_sort(array):
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array


print(selection_sort(arr))
