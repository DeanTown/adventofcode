def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    return stripped_lines