with open('day5_input.txt', 'r') as h:
    ranges_str, entries_str = h.read().strip().split('\n\n')

ranges = [[int(x) for x in r.split('-')] for r in ranges_str.split('\n')]
entries = [int(e) for e in entries_str.split('\n')]


def in_any_range(n, ranges):
    for r in ranges:
        if r[0] <= n <= r[1]:
            return True
    return False


def part1():
    print(sum(1 for e in entries if in_any_range(e, ranges)))


def try_union_ranges(a, b):
    if a[1] >= b[0] and b[1] >= a[0]:
        return [min(a[0], b[0]), max(a[1], b[1])]


def merge_ranges(ranges):
    ranges.sort(key=lambda r: r[0])
    i = 0
    while i + 1 < len(ranges):
        new_range = try_union_ranges(ranges[i], ranges[i+1])
        if new_range is not None:
            ranges[i] = new_range
            del ranges[i+1]
        else:
            i += 1


def part2():
    merge_ranges(ranges)
    print(sum(b - a + 1 for a, b in ranges))
