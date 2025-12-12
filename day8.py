with open('day8_input.txt', 'r') as h:
    points = [tuple(map(int, line.split(','))) for line in h]


def dist_sqr(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


edges = [(p, q) for i, p in enumerate(points)
         for q in points[i+1:]]
edges.sort(key=lambda e: dist_sqr(e[0], e[1]))


def extract_component(p, comps):
    for i, c in enumerate(comps):
        if p in c:
            return comps.pop(i)
    return {p}


def components(edges):
    comps = []
    for p, q in edges:
        p_comp = extract_component(p, comps)
        q_comp = extract_component(q, comps)
        comps.append(p_comp | q_comp)
    return comps


def part1():
    comps = components(edges[:1000])
    component_sizes = sorted([len(c) for c in comps], reverse=True)
    print(component_sizes[0] * component_sizes[1] * component_sizes[2])


def part2():
    to_connect = set(points)
    for p, q in edges:
        to_connect -= {p, q}
        if not to_connect:
            print(p[0] * q[0])
            break
