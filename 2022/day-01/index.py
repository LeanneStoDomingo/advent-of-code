import utils

puzzle_input = str(utils.get_input(2022, 1))

deer = puzzle_input.split('\n\n')

sum_calories = [sum([int(c or 0) for c in d.split('\n')]) for d in deer]

sum_calories = sorted(sum_calories, reverse=True)

print('Part one:', sum_calories[0])

print('Part two:', sum(sum_calories[:3]))
