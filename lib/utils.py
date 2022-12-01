def read_input(filename, split_lines=False):
    file = open(filename, 'r')
    if split_lines:
        return file.read().splitlines()
    return file.read()