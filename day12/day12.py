import re
from util import lcm


class Moon:
    def __init__(self, key, px=0, py=0, pz=0, vx=0, vy=0, vz=0):
        self.key = key
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __repr__(self):
        return f'id {self.key} pos: {self.px},{self.py},{self.pz} vel: {self.vx}, {self.vy}, {self.vz}'

    def __eq__(self, other):
        return self.key == other.key and self.px == other.px and self.py == other.py and self.pz == other.pz

    def potential_engergy(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

    def kinetic_engergy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)


def pprint(moons):
    for m in moons:
        print(m)


def load(coords):
    ret = []
    key = 'A'
    for c in coords:
        # d = [int(num) for num in re.split(r'\D || -\D', c) if num != '']
        d = [int(num) for num in re.split(r'[^-\d\d]', c) if num != '']
        ret.append(Moon(key, d[0], d[1], d[2]))
        key = chr(ord(key) + 1)
    return ret


def apply_gravity(moon, moons):
    gtx = len([m for m in moons if m.px > moon.px])
    gty = len([m for m in moons if m.py > moon.py])
    gtz = len([m for m in moons if m.pz > moon.pz])
    ltx = len([m for m in moons if m.px < moon.px])
    lty = len([m for m in moons if m.py < moon.py])
    ltz = len([m for m in moons if m.pz < moon.pz])
    vx = moon.vx + gtx - ltx
    vy = moon.vy + gty - lty
    vz = moon.vz + gtz - ltz
    px = moon.px + vx
    py = moon.py + vy
    pz = moon.pz + vz
    return Moon(moon.key, px, py, pz, vx, vy, vz)


def time_step(moons):
    moved_moons = []
    for i in range(0, len(moons)):
        m = moons.pop(0)
        moved_moons.append(apply_gravity(m, moons))
        moons.append(m)
    return moved_moons


def total_energy(moons):
    tot = 0
    for m in moons:
        tot = tot + m.potential_engergy() * m.kinetic_engergy()
    return tot


def part1(moons):
    for i in range(1, steps + 1):
        moons = time_step(moons)
    print('part1:', total_energy(moons))


def originals(key, original, curr):
    ret = True
    pkey = 'p' + key
    vkey = 'v' + key
    for i, o in enumerate(original):
        c = curr[i]
        if getattr(o, pkey) != getattr(c, pkey) or getattr(o, vkey) != getattr(c, vkey):
            ret = False
    return ret


def part2(moons):
    orig = moons.copy()
    x, y, z = False, False, False
    for i in range(1, steps + 1):
        moons = time_step(moons)
        if not x and originals('x', orig, moons):
            print(f'all xs are back to original at step {i}')
            x_cycle = i
            x = True
        if not y and originals('y', orig, moons):
            print(f'all ys are back to original at step {i}')
            y_cycle = i
            y = True
        if not z and originals('z', orig, moons):
            print(f'all zs are back to original at step {i}')
            z_cycle = i
            z = True
        if x and y and z:
            ans = lcm(x_cycle, lcm(y_cycle, z_cycle))
            # part 2 374307970285176
            print(f'part 2: {ans}')
            break


# inp = ['<x=-1, y=0, z=2>', '<x=2, y=-10, z=-7>', '<x=4, y=-8, z=8>', '<x=3, y=5, z=-1>']  # test
# inp = ['<x=-8, y=-10, z=0>', '<x=5, y=5, z=10>', '<x=2, y=-7, z=3>', '<x=9, y=-8, z=-3>']  # test2
inp = ['<x=16, y=-11, z=2>','<x=0, y=-4, z=7>','<x=6, y=4, z=-10>','<x=-3, y=-2, z=-4>']  # prod
# steps = 100
# steps = 2772
steps = 1000000
moons = load(inp)
print('step 0 moons', moons)
part2(moons)

