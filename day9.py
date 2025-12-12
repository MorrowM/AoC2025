from itertools import combinations

with open('day9_input.txt', 'r') as h:
    points = [tuple(map(int, line.split(',')))
              for line in h]


def rect_area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def part1():
    print(max(rect_area(p, q) for p, q in combinations(points, 2)))


def intersects_open_closed(i, j, k, l):
    # Does the closed interval [k,l] intersect the open interval (i,j)?
    i, j = sorted([i, j])
    k, l = sorted([k, l])
    return l > i and k < j


def intersects_rect_interior(r, s, p, q):
    # Does the line segment rs intersect the interior of the rectangle defined by p and q?
    x = int(r[1] == s[1])  # the shared coordinate
    y = 1 - x  # the other coordinate
    p, q = sorted([p, q], key=lambda t: t[x])
    return p[x] < r[x] < q[x] and intersects_open_closed(p[y], q[y], r[y], s[y])


def valid_rect(p, q):
    wrapped = points + [points[0]]
    return not any(intersects_rect_interior(r, s, p, q) for r, s in zip(wrapped, wrapped[1:]))


def part2():
    print(max((rect_area(p, q)
          for p, q in combinations(points, 2) if valid_rect(p, q))))
