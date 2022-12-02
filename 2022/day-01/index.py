import utils

puzzle_input = str(utils.get_input(2022, 1))

deer = puzzle_input.split('\n\n')

sum_calories = []

for d in deer:
    calories_text = d.split('\n')
    calories = [int(c or 0) for c in calories_text]
    total_calories = sum(calories)
    sum_calories.append(total_calories)

sum_calories = sorted(sum_calories, reverse=True)

print(f'The highest total calories is {sum_calories[0]}')

print(f'The sum of the top three calories is {sum(sum_calories[:3])}')
