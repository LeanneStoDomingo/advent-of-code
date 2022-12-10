import utils

puzzle_input = str(utils.get_input(2022, 10))


instructions = puzzle_input.strip().split('\n')

cycle = 1
X = 1
total_signal_strength = 0

for instruction in instructions:
    if (cycle - 20) % 40 == 0:
        total_signal_strength += X * cycle

    if instruction != 'noop':
        num = int(instruction.split(' ')[1])

        cycle += 1

        if (cycle - 20) % 40 == 0:
            total_signal_strength += X * cycle

        cycle += 1

        X += num
    else:
        cycle += 1


print('Part one:', total_signal_strength)


cycle = 1
X = 1

print('Part two:')


for instruction in instructions:
    if X - 1 == (cycle - 1) % 40 or X == (cycle - 1) % 40 or X + 1 == (cycle - 1) % 40:
        print('#', end='')
    else:
        print('.', end='')

    if cycle % 40 == 0:
        print()

    if instruction != 'noop':
        num = int(instruction.split(' ')[1])

        cycle += 1

        if X - 1 == (cycle - 1) % 40 or X == (cycle - 1) % 40 or X + 1 == (cycle - 1) % 40:
            print('#', end='')
        else:
            print('.', end='')

        if cycle % 40 == 0:
            print()

        cycle += 1

        X += num
    else:
        cycle += 1
