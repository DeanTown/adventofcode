from lib.utils import read_input
from functools import reduce
import operator


op_map = {
    "+": operator.add,
    "*": operator.mul,
}


class Monkey:
    def __init__(
        self,
        number,
        items,
        op,
        op_value,
        test_value,
        target_true,
        target_false,
    ):
        self.number = number
        self.items = items
        self.op = op
        self.op_value = op_value
        self.test_value = test_value
        self.target_true = target_true
        self.target_false = target_false
        self.inspections = 0

    def __repr__(self):
        return f"""
Monkey {self.number}:
    Items: {self.items}
    Operation: new = old {self.op} {self.op_value}
    Test: divisible by {self.test_value}
        If true: throw to monkey {self.target_true}
        If false: throw to monkey {self.target_false}
        """


def go():
    input = read_input("input/2022:11.txt")
    monkeys = parse_input(input)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop(0)
                # inspect the item
                monkey.inspections += 1
                # increase worry level
                op_value = item if monkey.op_value == "old" else int(monkey.op_value)
                item = monkey.op(item, op_value)
                # decrease worry level
                item = item // 3
                # perform test and throw to new monkey
                target = None
                if item % monkey.test_value == 0:
                    target = monkey.target_true
                else:
                    target = monkey.target_false
                monkeys[target].items.append(item)

    monkey_inspections = [monkey.inspections for monkey in monkeys]
    monkey_inspections = sorted(monkey_inspections, reverse=True)[:2]

    return reduce(lambda x, y: x * y, monkey_inspections), False


def parse_input(input):
    monkeys = []
    split = input.split("\n\n")
    split = [item.split("\n") for item in split]
    for i in range(len(split)):
        values = split[i]
        # parse items
        items = values[1].split(":")
        items = items[1].split(",")
        items = [int(item.strip()) for item in items]
        # parse operation
        operation = values[2].split("=")
        operation = operation[1].split()
        op = op_map.get(operation[1])
        op_value = operation[2]
        # parse test
        test_value = int(values[3].split()[-1])
        # parse targets
        target_true = int(values[4].split()[-1])
        target_false = int(values[5].split()[-1])

        monkeys.append(
            Monkey(
                number=i,
                items=items,
                op=op,
                op_value=op_value,
                test_value=test_value,
                target_true=target_true,
                target_false=target_false,
            )
        )
    return monkeys


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
