from scipy import optimize
import numpy as np


def parse_line(line):
    lights, rest = line[1:].split(']')
    lights = [l == '#' for l in lights]
    buttons, joltages = rest.split('{')
    buttons = buttons.strip().split(' ')
    buttons = [[int(x) for x in b[1:-1].split(',')] for b in buttons]
    joltages = joltages[:-2].split(',')
    joltages = [int(j) for j in joltages]

    return lights, buttons, joltages


with open('day10_input.txt', 'r') as h:
    data = [parse_line(line) for line in h]


def press_button(lights, button):
    new_lights = lights[:]
    for i in button:
        new_lights[i] = not new_lights[i]
    return new_lights


def solve(lights, buttons, joltages):
    step = 0
    light_states = [[False] * len(lights)]
    while lights not in light_states:
        step += 1
        new_light_states = []
        for light in light_states:
            for button in buttons:
                new_light_states.append(press_button(light, button))
        light_states = new_light_states
    return step


def part1():
    print(sum(solve(*prob) for prob in data))


def solve2(lights, buttons, joltages):
    c = np.array([1] * len(buttons), dtype=int)
    bounds = optimize.Bounds(0, np.inf)
    A = np.array([[int(i in b) for i in range(len(joltages))]
                 for b in buttons], dtype=int).T
    constraints = optimize.LinearConstraint(A=A, lb=joltages, ub=joltages)
    res = optimize.milp(c, integrality=1, bounds=bounds,
                        constraints=constraints)
    return int(res.fun)


def part2():
    print(sum(solve2(*prob) for prob in data))
