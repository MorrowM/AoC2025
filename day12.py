present_sizes = [7, 7, 6, 7, 5, 7]


def parse_line(l):
    x = int(l[:2])
    y = int(l[3:5])
    amounts = [int(a) for a in l[7:].strip().split()]
    return (x, y, amounts)


with open('day12_input.txt', 'r') as h:
    info = [parse_line(l) for l in h.readlines()]


def can_fit_maybe(x, y, amounts):
    return x * y >= sum(amount * size for amount, size in zip(amounts, present_sizes))


def part1():
    print(sum(1 for x, y, amounts in info if can_fit_maybe(x, y, amounts)))
