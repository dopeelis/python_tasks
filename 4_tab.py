space = ' ' * 4


def tab_to_space(file):
    with open(file) as old_file, open('tab_output.txt', 'w') as new_file:
        for line in old_file:
            new_line = line.replace('\t', space)
            new_file.write(new_line)


def space_to_tab(file):
    with open(file) as old_file, open('space_output.txt', 'w') as new_file:
        for line in old_file:
            new_line = line.replace(space, '\t')
            new_file.write(new_line)


