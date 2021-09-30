arr = [10, 20, 30, 40]
string = '123546'
data = {'one': '1', 'two': '2'}


def enumeration(collection):
    count = 0
    output = []
    for element in collection:
        output.append((count, element))
        count += 1
    return output


for i in enumeration([3, 2, 1]):
    print(i)

