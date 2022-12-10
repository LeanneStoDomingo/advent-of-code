import utils

puzzle_input = str(utils.get_input(2022, 9))

instructions = [[x.split(' ')[0], int(x.split(' ')[1])] for x in puzzle_input.strip().split('\n') if x != '']


H_x = 0
H_y = 0
T_x = 0
T_y = 0

visited = ['0, 0']

for instruction in instructions:
    for i in range(instruction[1]):
        if instruction[0] == 'R':
            H_x += 1
        elif instruction[0] == 'L':
            H_x -= 1
        elif instruction[0] == 'U':
            H_y += 1
        elif instruction[0] == 'D':
            H_y -= 1

        if not (T_x == H_x and T_y == H_y) and not (T_x == H_x + 1 and T_y == H_y) and not (T_x == H_x - 1 and T_y == H_y) and not (T_x == H_x and T_y == H_y + 1) and not (T_x == H_x and T_y == H_y - 1) and not (T_x == H_x + 1 and T_y == H_y + 1) and not (T_x == H_x - 1 and T_y == H_y - 1) and not (T_x == H_x + 1 and T_y == H_y - 1) and not (T_x == H_x - 1 and T_y == H_y + 1):
            if T_x == H_x:
                if T_y < H_y:
                    T_y += 1
                else:
                    T_y -= 1
            elif T_y == H_y:
                if T_x < H_x:
                    T_x += 1
                else:
                    T_x -= 1
            else:
                if T_x < H_x:
                    T_x += 1
                else:
                    T_x -= 1
                if T_y < H_y:
                    T_y += 1
                else:
                    T_y -= 1

        visited.append(f'{T_x}, {T_y}')


print('Part one:', len(set(visited)))


H_x = 0
H_y = 0

knots = [[0, 0] for _ in range(9)]

visited = ['0, 0']

for instruction in instructions:
    for i in range(instruction[1]):
        if instruction[0] == 'R':
            H_x += 1
        elif instruction[0] == 'L':
            H_x -= 1
        elif instruction[0] == 'U':
            H_y += 1
        elif instruction[0] == 'D':
            H_y -= 1

        for j in range(len(knots)):
            T_x = knots[j][0]
            T_y = knots[j][1]
            P_x = knots[j - 1][0] if j > 0 else H_x
            P_y = knots[j - 1][1] if j > 0 else H_y

            if not (T_x == P_x and T_y == P_y) and not (T_x == P_x + 1 and T_y == P_y) and not (T_x == P_x - 1 and T_y == P_y) and not (T_x == P_x and T_y == P_y + 1) and not (T_x == P_x and T_y == P_y - 1) and not (T_x == P_x + 1 and T_y == P_y + 1) and not (T_x == P_x - 1 and T_y == P_y - 1) and not (T_x == P_x + 1 and T_y == P_y - 1) and not (T_x == P_x - 1 and T_y == P_y + 1):
                if T_x == P_x:
                    if T_y < P_y:
                        T_y += 1
                    else:
                        T_y -= 1
                elif T_y == P_y:
                    if T_x < P_x:
                        T_x += 1
                    else:
                        T_x -= 1
                else:
                    if T_x < P_x:
                        T_x += 1
                    else:
                        T_x -= 1
                    if T_y < P_y:
                        T_y += 1
                    else:
                        T_y -= 1

            knots[j][0] = T_x
            knots[j][1] = T_y

            if j > 0:
                knots[j - 1][0] = P_x
                knots[j - 1][1] = P_y

        visited.append(f'{knots[8][0]}, {knots[8][1]}')

print('Part two:', len(set(visited)))
