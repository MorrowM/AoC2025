def neighbors(cell):
    i, j = cell
    return {(i + dx, j + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0}


def accessible(cells):
    return {cell for cell in cells if len(neighbors(cell) & cells) < 4}


with open('day4_input.txt', 'r') as h:
    cells = {(i, j) for i, line in enumerate(h)
             for j, sym in enumerate(line) if sym == '@'}


def part1():
    print(len(accessible(cells)))


def part2():
    removed = 0
    while True:
        to_remove = accessible(cells)
        if to_remove:
            cells.difference_update(to_remove)
            removed += len(to_remove)
        else:
            break

    print(removed)
