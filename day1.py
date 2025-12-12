def parse_line(l):
    l = l.strip()
    mult = 1 if l[0] == 'R' else -1
    return mult * int(l[1:])

def mod(a,m):
    return (a % m + m) % m

with open('day1_input.txt', 'r') as h:
    inp = map(parse_line, h.readlines())


password = 0
pos = 50
for diff in inp:    
    # Part 2:
    password += abs(pos + diff) // 100 \
             + (1 if pos > 0 and pos + diff <= 0 else 0)

    pos = mod(pos + diff, 100)

    # Part 1:
    # password += int(pos == 0)
    
print(password)
