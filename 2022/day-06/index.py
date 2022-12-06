import utils

puzzle_input = str(utils.get_input(2022, 6))


def solve(puzzle_input, unique_count):
    possible_marker = puzzle_input[:unique_count]

    for i in range(unique_count, len(puzzle_input)):
        if len(set(possible_marker)) == unique_count:
            return i
        else:
            possible_marker += puzzle_input[i]
            possible_marker = possible_marker[1:]


print('Part one:', solve(puzzle_input, 4))
print('Part two:', solve(puzzle_input, 14))
