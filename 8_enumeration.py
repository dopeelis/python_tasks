arr = [10, 20, 30, 40]
string = '123546'
data = {'one': '1', 'two': '2'}


def enumeration(collection):
    output = []
    try:
        for i in range(len(collection)):
            output.append((i, collection[i]))
        return output
    except KeyError:
        i = 0
        for key in collection:
            output.append((i, key))
            i += 1
        return output


print(enumeration(string))
