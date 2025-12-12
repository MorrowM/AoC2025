with open('day7_input.txt', 'r') as h:
    lines = h.readlines()


def part1():
    flows = {lines[0].find('S')}
    num_splits = 0
    for line in lines[1:]:
        new_flows = {flow for flow in flows}
        for j, c in enumerate(line):
            if c == '^' and j in flows:
                new_flows.remove(j)
                new_flows.add(j - 1)
                new_flows.add(j + 1)
                num_splits += 1

        flows = new_flows

    print(num_splits)


def part2():
    path_counts = [int(c == 'S') for c in lines[0]]

    for i, l in enumerate(lines[1:], start=1):
        new_path_counts = [0] * len(l)
        for j, c in enumerate(l):
            match c:
                case '.':
                    new_path_counts[j] += path_counts[j]
                case '^':
                    new_path_counts[j - 1] += path_counts[j]
                    new_path_counts[j + 1] += path_counts[j]

        path_counts = new_path_counts

    print(sum(path_counts))
