test = ['111111', '122345', '111123', '223450', '123789']
test2 = ['112233', '12344456', '11112211']
data = '152085-670283'
inp = [int(x) for x in data.split('-')]


def valid(num):
    prev = '0'
    dups = set()
    for c in (str(num)):
        if c == prev:
            dups.add(c)
        if c >= prev:
            prev = c
        else:
            return False
    if len(dups) >= 1:
        return True
    else:
        return False


def part2(num):
    prev = str(num)[0]
    ct = 1
    for c in str(num)[1:]:
        if c == prev:
            ct += 1
        else:
            if ct == 2:
                return True
            else:
                ct = 1
                prev = c
    if ct == 2:
        return True
    else:
        return False


# part1 1764
part = 1
print('range:', inp)
p1 = list(filter(valid, range(inp[0], inp[1] + 1)))
print('part1:', len(p1))

p2 = list(filter(part2, p1))
print('part2:', len(p2))