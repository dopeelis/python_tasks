example = [[1, 2, 4], [5, 6, 7]]


def delete_column(number, list_of_lists):
    column = None
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if list_of_lists[i][j] == number:
                column = j
                break
        break
    for i in range(len(list_of_lists)):
        list_of_lists = list_of_lists.pop([i][column])
    print(list_of_lists)


delete_column(2, example)