import utils

puzzle_input = str(utils.get_input(2022, 2)).split('\n')

play = [a.split() for a in puzzle_input]

total = 0

for p in play:
    if len(p) != 2:
        continue

    me = p[1]
    them = p[0]

    if me == 'X':
        total += 1
        if them == 'A':
            total += 3
        elif them == 'C':
            total += 6
    elif me == 'Y':
        total += 2
        if them == 'B':
            total += 3
        elif them == 'A':
            total += 6
    elif me == 'Z':
        total += 3
        if them == 'C':
            total += 3
        elif them == 'B':
            total += 6

print(f'Part one: {total}')


total = 0

tie = {
    'A': 1,
    'B': 2,
    'C': 3,
}

lose = {
    'A': 3,
    'B': 1,
    'C': 2,
}

win = {
    'A': 2,
    'B': 3,
    'C': 1,
}

for p in play:
    if len(p) != 2:
        continue

    me = p[1]
    them = p[0]

    if me == 'X':
        total += lose[them]
    elif me == 'Y':
        total += 3
        total += tie[them]
    elif me == 'Z':
        total += 6
        total += win[them]

print(f'Part two: {total}')
