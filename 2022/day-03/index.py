import utils

puzzle_input = str(utils.get_input(2022, 3))

rucksacks = puzzle_input.split('\n')

total = 0

for r in rucksacks:
    first = set(list(r[:int(len(r)/2)]))
    second = set(list(r[int(len(r)/2):]))

    for f in first:
        if f in second:
            c = ord(f)

            if c < 91:
                total += c - 38
            else:
                total += c - 96


print('Part one:', total)

total = 0

j = 0

groups = []

for i in range(len(rucksacks)):
    if i % 3 == 0:
        groups.append([])
        groups[j].append(rucksacks[i])
    elif i % 3 == 2:
        groups[j].append(rucksacks[i])
        j += 1
    else:
        groups[j].append(rucksacks[i])

for g in groups:
    if len(g) != 3:
        continue

    first = set(list(g[0]))
    second = set(list(g[1]))
    third = set(list(g[2]))

    for f in first:
        if f in second and f in third:
            c = ord(f)

            if c < 91:
                total += c - 38
            else:
                total += c - 96

print('Part two:', total)
