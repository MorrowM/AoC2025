
def parse_line(l):
    i, o = l.strip().split(':')
    return i, o.strip().split()


with open('day11_input.txt', 'r') as h:
    io = {i: set(o) for i, o in (parse_line(l) for l in h)}


def calc_paths(src, target):
    paths_to = {src: 1}

    def go(x):
        if x in paths_to:
            return paths_to[x]

        res = sum(go(i) for i, o in io.items() if x in o)
        paths_to[x] = res
        return res
    return go(target)


def part1():
    print(calc_paths('you', 'out'))


def part2():
    print(calc_paths('svr', 'dac') * calc_paths('dac', 'fft') * calc_paths('fft', 'out') +
          calc_paths('svr', 'fft') * calc_paths('fft', 'dac') * calc_paths('dac', 'out'))
