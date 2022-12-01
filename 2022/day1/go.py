from lib.utils import read_input

input = read_input("2022/day1/input.txt", split_lines=True)

# PART 1

calorie_counts = [0]
for line in input:
    if line == '':
        calorie_counts.append(0)
    else:
        calorie_counts[-1] += int(line)

print(max(calorie_counts))

# PART 2

sorted_counts = sorted(calorie_counts, reverse=True)[:3]
print(sum(sorted_counts))