from lib.utils import read_input


def go():
    input = read_input("input/2020:4.txt")
    input = [line.replace("\n", " ") for line in input.split("\n\n")]

    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    part1 = 0
    part2 = 0
    for line in input:
        if all(_ in line for _ in req_fields):
            part1 += 1
            batch = dict([_.split(":") for _ in line.split()])
            batch_res = 1
            for key, value in batch.items():
                validate_func = f"validate_{key}"
                res = getattr(Validation, validate_func)(value)
                if not res:
                    batch_res = 0
            part2 += batch_res

    return part1, part2


class Validation:
    def validate_byr(value):
        # four digits; at least 1920 and at most 2002
        if not len(value) == 4:
            return False
        if not 1920 <= int(value) <= 2002:
            return False
        return True

    def validate_iyr(value):
        # four digits; at least 2010 and at most 2020
        if not len(value) == 4:
            return False
        if not 2010 <= int(value) <= 2020:
            return False
        return True

    def validate_eyr(value):
        # four digits; at least 2020 and at most 2030
        if not len(value) == 4:
            return False
        if not 2020 <= int(value) <= 2030:
            return False
        return True

    def validate_hgt(value):
        # a number followed by either cm or in; if cm, the number must be at least 150 and at most 193; if in, the number must be at least 59 and at most 76
        try:
            unit = value[-2:]
            val = int(value[:-2])
        except:
            return False
        if unit == "in":
            if not 59 <= val <= 76:
                return False
        if unit == "cm":
            if not 150 <= val <= 193:
                return False
        return True

    def validate_hcl(value):
        # a # followed by exactly six characters 0-9 or a-f
        if not value[0] == "#":
            return False
        value = value[1:]
        if not len(value) == 6:
            return False
        if not all(_ in "0123456789abcdef" for _ in value):
            return False
        return True

    def validate_ecl(value):
        # exactly one of: amb, blu, brn, gry, grn, hzl, oth
        if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        return True

    def validate_pid(value):
        # a nine-digit number, including leading zeros
        if not (len(value) == 9 and value.isnumeric()):
            return False
        return True

    def validate_cid(value):
        return True


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
