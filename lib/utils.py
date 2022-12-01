def read_input(filename, split_lines=False):
    file = open(filename, 'r')
    read = file.read()
    file.close()
    if split_lines:
        return read.splitlines()
    return read