
with open('day3_input.txt', 'r') as h:
    banks = [l.strip() for l in h.readlines()]


def max_power(bank, bats):
    digs = []
    i = -1
    for k in range(bats):
        print(i + 1, k - bats + 1)
        i_new, d = max(enumerate(bank[i+1:len(bank) - bats + k + 1],
                                 start=i+1), key=lambda x: (x[1], -x[0]))
        i = i_new
        digs.append(d)
    print(digs)
    return int(''.join(digs))


def part1():
    print(sum(max_power(b, 2) for b in banks))


def part2():
    print(sum(max_power(b, 12) for b in banks))
