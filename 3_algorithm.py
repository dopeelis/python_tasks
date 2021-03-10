arr = [0, 3, 24, 2, 3, 7]


def min_to_max(func):
    for i in range(len(func)):
        minimum_index = i
        for j in range(i+1, len(func)):
            if func[j] < func[minimum_index]:
                minimum_index = j
        func[i], func[minimum_index] = func[minimum_index], func[i]
    print(func)


min_to_max(arr)
