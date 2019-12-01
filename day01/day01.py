import util

inp = util.get_number_input(True, '01')


def mass_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return mass
    return fuel + mass_fuel(fuel)


# part1: 3270717
p1 = sum([n//3 - 2 for n in inp])
print("part1:", p1)

# part2:  4903193
p2 = sum([mass_fuel(num) for num in inp])
print("part2: ", p2)


