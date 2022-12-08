import utils

puzzle_input = str(utils.get_input(2022, 8))

rows = [[int(x) for x in row] for row in puzzle_input.strip().split('\n')]

part_one = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if i == 0 or i == len(rows) - 1 or j == 0 or j == len(rows[i]) - 1:
            part_one += 1
        else:
            above_visible = True
            below_visible = True
            left_visible = True
            right_visible = True
            for k in range(i):
                if rows[k][j] >= rows[i][j]:
                    above_visible = False
            for k in range(i + 1, len(rows)):
                if rows[k][j] >= rows[i][j]:
                    below_visible = False
            for k in range(j):
                if rows[i][k] >= rows[i][j]:
                    left_visible = False
            for k in range(j + 1, len(rows[i])):
                if rows[i][k] >= rows[i][j]:
                    right_visible = False
            if above_visible or below_visible or left_visible or right_visible:
                part_one += 1

print('Part one:', part_one)


part_two = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if not (i == 0 or i == len(rows) - 1 or j == 0 or j == len(rows[i]) - 1):
            above_visible = 0
            below_visible = 0
            left_visible = 0
            right_visible = 0
            for k in reversed(range(i)):
                if rows[k][j] < rows[i][j]:
                    above_visible += 1
                else:
                    above_visible += 1
                    break
            for k in range(i + 1, len(rows)):
                if rows[k][j] < rows[i][j]:
                    below_visible += 1
                else:
                    below_visible += 1
                    break
            for k in reversed(range(j)):
                if rows[i][k] < rows[i][j]:
                    left_visible += 1
                else:
                    left_visible += 1
                    break
            for k in range(j + 1, len(rows[i])):
                if rows[i][k] < rows[i][j]:
                    right_visible += 1
                else:
                    right_visible += 1
                    break

            score = above_visible * below_visible * left_visible * right_visible

            if score > part_two:
                part_two = score


print('Part two:', part_two)
