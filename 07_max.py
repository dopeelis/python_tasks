def find_max(*args, **kwargs):
    values = []
    for i in args:
        if isinstance(i, list):
            values.extend(i)
        else:
            values.append(i)
    values.extend(kwargs.values())
    maximum = values[0]
    for n in values:
        if n <= maximum:
            continue
        maximum = n
    return maximum


print(find_max([1, 2, 9]))
