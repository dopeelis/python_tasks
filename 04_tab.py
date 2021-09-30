import fileinput


def replace_tab_space(file, old_symbol, new_symbol):
    with fileinput.input(file, inplace=True) as f:
        for line in f:
            new_line = line.replace(old_symbol, new_symbol)
            print(new_line, end='')
