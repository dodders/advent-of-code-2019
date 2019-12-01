import util


def mass_fuel(num):
    ret = []
    while num > 0:
        num = num // 3 - 2
        if num > 0:
            ret.append(num)
    return ret


inp = util.get_number_input(True, '01')
p1 = sum([n//3 - 2 for n in inp])
print("part1:", p1)

p2 = sum([sum(mass_fuel(num)) for num in inp])
print("part2: ", p2)



