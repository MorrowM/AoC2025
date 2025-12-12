
with open('day2_input.txt', 'r') as h:
    ranges = [tuple(map(int, r.split('-'))) for l in h for r in l.split(',')]


def is_dup_str(s):
    n = len(s) // 2
    return s[:n] == s[n:]


def part1():
    print(sum(i for a, b in ranges for i in range(a, b + 1) if is_dup_str(str(i))))


def is_repeat_str(s):
    for i in range(1, len(s)):
        if s[:i] * (len(s) // i) == s:
            return True
    return False


def part2():
    print(sum(i for a, b in ranges for i in range(
        a, b + 1) if is_repeat_str(str(i))))
