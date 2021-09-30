example = [
    [1, 2, 4],
    [5, 6, 7]
]


def delete_column(number, list_of_lists):
    column = None
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if list_of_lists[i][j] == number:
                column = j
    for i in range(len(list_of_lists)):
        del list_of_lists[i][column]
    return list_of_lists


print(delete_column(7, example))