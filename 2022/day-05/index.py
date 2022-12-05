import utils

puzzle_input = str(utils.get_input(2022, 5))

x = puzzle_input.split('\n\n')

pile_lines = x[0].split('\n')

pile_lines = [[p[i:i+4].strip() for i in range(0, len(p), 4)] for p in pile_lines]

moves = x[1].split('\n')


piles = [[] for i in range(int(pile_lines[-1][-1]))]

for i in range(len(pile_lines) - 1):
    for j in range(len(pile_lines[i])):
        crate = pile_lines[i][j]
        if crate != '':
            piles[j].append(crate[1:-1])

piles = [list(reversed(p)) for p in piles]


for move in moves:
    if move == '':
        continue

    move = move.split(' ')

    amount = int(move[1])
    from_pile = int(move[3])
    to_pile = int(move[5])

    for i in range(amount):
        piles[to_pile - 1].append(piles[from_pile - 1].pop())


part_one = ''

for pile in piles:
    part_one += pile[-1]

print('Part one:', part_one)


piles = [[] for i in range(int(pile_lines[-1][-1]))]

for i in range(len(pile_lines) - 1):
    for j in range(len(pile_lines[i])):
        crate = pile_lines[i][j]
        if crate != '':
            piles[j].append(crate[1:-1])

piles = [list(reversed(p)) for p in piles]


for move in moves:
    if move == '':
        continue

    move = move.split(' ')

    amount = int(move[1])
    from_pile = int(move[3])
    to_pile = int(move[5])

    temp_pile = []

    for i in range(amount):
        temp_pile.append(piles[from_pile - 1].pop())

    temp_pile = list(reversed(temp_pile))

    for i in range(len(temp_pile)):
        piles[to_pile - 1].append(temp_pile[i])

part_two = ''

for pile in piles:
    part_two += pile[-1]

print('Part two:', part_two)
