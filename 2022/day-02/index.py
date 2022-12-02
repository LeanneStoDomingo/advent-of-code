import utils

puzzle_input = str(utils.get_input(2022, 2)).split('\n')

play = [a.split() for a in puzzle_input]

total = 0

score = {
    'X': {
        'A': 3 + 1,
        'B': 0 + 1,
        'C': 6 + 1,
    },
    'Y': {
        'A': 6 + 2,
        'B': 3 + 2,
        'C': 0 + 2,
    },
    'Z': {
        'A': 0 + 3,
        'B': 6 + 3,
        'C': 3 + 3,
    },
}

for p in play:
    if len(p) == 2:
        total += score[p[1]][p[0]]

print('Part one:', total)


total = 0

score = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2,
    },
    'Y': {
        'A': 1 + 3,
        'B': 2 + 3,
        'C': 3 + 3,
    },
    'Z': {
        'A': 2 + 6,
        'B': 3 + 6,
        'C': 1 + 6,
    }
}


for p in play:
    if len(p) == 2:
        total += score[p[1]][p[0]]


print('Part two:', total)
