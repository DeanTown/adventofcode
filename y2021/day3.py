from lib.utils import read_input


def go():
    input = read_input("input/2021:3.txt", split_lines=True)

    # PART 1
    gamma = ""

    for i in range(len(input[0])):
        index_list = [line[i] for line in input]
        gamma += max(set(index_list), key=index_list.count)
    epsilon = gamma.replace("0", "2")
    epsilon = epsilon.replace("1", "0")
    epsilon = epsilon.replace("2", "1")
    part1 = int(gamma, 2) * int(epsilon, 2)

    # PART 2
    def reduce(lst, least_common=False):
        for i in range(len(lst[0])):
            index_list = [line[i] for line in lst]
            zeros = index_list.count("0")
            ones = index_list.count("1")
            bit = ""
            if least_common:
                bit = "0" if zeros <= ones else "1"
            else:
                bit = "1" if ones >= zeros else "0"
            if len(lst) > 1:
                lst = list(filter(lambda x: x[i] == bit, lst))
        return lst[0]

    most_common = reduce(input)
    least_common = reduce(input, least_common=True)
    part2 = int(most_common, 2) * int(least_common, 2)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
