import functools

with open('day6_input.txt') as h:
    data = zip(*(line.split() for line in h))

ops = {'+': int.__add__, '*': int.__mul__}


def eval_prob(prob):
    return functools.reduce(ops[prob[-1]], map(int, prob[:-1]))


def part1():
    print(sum(eval_prob(prob) for prob in data))


def split_list(lst, cond):
    chunks = []
    curr_chunk = []
    for x in lst:
        if cond(x):
            chunks.append(curr_chunk)
            curr_chunk = []
        else:
            curr_chunk.append(x)

    if curr_chunk:
        chunks.append(curr_chunk)
    return chunks


with open('day6_input.txt') as h:
    data = h.readlines()
    op_strs = data[-1].strip().split()
    numss = split_list((''.join(x)
                       for x in zip(*data[:-1])), lambda s: s.strip() == '')


def eval_prob2(prob):
    op, nums = prob
    return functools.reduce(ops[op], (int(n.strip()) for n in nums))


def part2():
    print(sum(eval_prob2(prob) for prob in zip(op_strs, numss)))
