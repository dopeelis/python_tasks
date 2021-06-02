def not_generation_func_1(m, source=None):
    if source is None:
        source = [1, 2, 3]
    result = []
    for i in range(len(source)):
        result.append(source[i] * m)
    return result


print(not_generation_func_1(3, [10, 11, 12]))


def generation_func_1(m, source=None):
    if source is None:
        source = [1, 2, 3]
    result = (m * source[i] for i in range(len(source)))
    for j in result:
        print(j, end=' ')


def generation_func_2(m, source=None):
    if source is None:
        source = [1, 2, 3]
    for i in range(len(source)):
        yield m * source[i]


generation_func_1(2, [4, 10, 44])


for i in generation_func_2(2, [4, 10, 44]):
    print(i)
