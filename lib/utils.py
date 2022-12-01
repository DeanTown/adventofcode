def read_input(filename, split_lines=False, convert_to_num=False):
    file = open(filename, 'r')
    read = file.read()
    file.close()
    if split_lines:
        return read.splitlines()
    if convert_to_num:
        lines = read.splitlines()
        return [int(line) for line in lines]
    return read