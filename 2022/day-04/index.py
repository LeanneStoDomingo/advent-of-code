import utils

puzzle_input = str(utils.get_input(2022, 4))

x = puzzle_input.split('\n')

total = 0

ranges = [[[int(c) for c in b.split('-') if c != ''] for b in a.split(',')] for a in x]

for r in ranges:
    if len(r) != 2:
        continue

    first = r[0]
    second = r[1]

    if len(first) != 2 or len(second) != 2:
        continue

    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        total += 1

print('Part one:', total)


total = 0

for r in ranges:
    if len(r) != 2:
        continue

    first = r[0]
    second = r[1]

    if len(first) != 2 or len(second) != 2:
        continue

    if (first[1] >= second[0] and first[0] <= second[1]) or (second[1] >= first[0] and second[0] <= first[1]):
        total += 1

print('Part two:', total)
