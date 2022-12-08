import utils

puzzle_input = str(utils.get_input(2022, 7))


lines = [x.split(' ') for x in puzzle_input.split('\n')]


class Tree:
    def __init__(self, name, parent=None, type='file', size=0):
        self.children = []
        self.name = name
        self.size = size
        self.type = type
        self.parent = parent


def find_shape():
    root = Tree('/', type='dir')
    curr_dir = root

    for line in lines[2:]:
        if line[0] == '':
            continue
        elif line[0] != '$':
            item = Tree(line[1], curr_dir)

            if line[0] == 'dir':
                item.type = 'dir'
            else:
                item.size = int(line[0])

            curr_dir.children.append(item)
        elif line[1] == 'cd':
            if line[2] == '..':
                curr_dir = curr_dir.parent
            else:
                curr_dir = [x for x in curr_dir.children if x.name == line[2] and x.type == 'dir'][0]

    return root


dir = find_shape()


def find_dir_size(root):
    if len(root.children) == 0:
        return root.size

    for leaf in root.children:
        root.size += find_dir_size(leaf)

    return root.size


find_dir_size(dir)


def find_less_than(root):
    t = []

    if root.size <= 100000:
        t += [root]

    for leaf in root.children:
        if leaf.type == 'dir':
            t += find_less_than(leaf)

    return t


part_one = find_less_than(dir)

print('Part one:', sum([x.size for x in part_one]))


def get_all_dirs(root):
    t = []

    if root.type == 'dir':
        t += [root]

    for leaf in root.children:
        if leaf.type == 'dir':
            t += get_all_dirs(leaf)

    return t


dirs = sorted(get_all_dirs(dir), key=lambda x: x.size)


unused = 70000000 - dir.size
free_up = 30000000 - unused

least_dir = None

for d in dirs:
    if d.size > free_up:
        least_dir = d
        break


print('Part two:', least_dir.size)
