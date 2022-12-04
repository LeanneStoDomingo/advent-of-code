import utils

puzzle_input = str(utils.get_input(2022, 4))

x = puzzle_input.split('\n')

total_one = 0
total_two = 0

ranges = [[[int(c) for c in b.split('-') if c != ''] for b in a.split(',')] for a in x]

for r in ranges:
    if len(r) != 2:
        continue

    first = r[0]
    second = r[1]

    if len(first) != 2 or len(second) != 2:
        continue

    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        total_one += 1

    if first[1] >= second[0] and first[0] <= second[1]:
        total_two += 1


print('Part one:', total_one)

print('Part two:', total_two)
