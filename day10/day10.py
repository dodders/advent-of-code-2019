import util
from util import Point


def parse(inp):
    g = []
    mx = len(inp[0])
    my = len(inp)
    for y, line in enumerate(inp):
        for x, point in enumerate(line):
            if point == '#':
                g.append(Point(x, y))
    return g, mx, my


def can_see(origin, points):
    sees = []
    points.remove(origin)
    angles = {}
    for point in points:
        angle = origin.angle(point)
        existing = angles.get(angle, None)
        if existing is None:
            angles[angle] = (origin, point, origin.distance(point))
        else:
            if origin.distance(point) < existing[2]:
                angles[angle] = (origin, point, origin.distance(point))
    for e in angles.values():
        sees.append(e[1])
    return sees


def pprint(sees):
    for y in range(0, maxy):
        for x in range(0, maxx):
            points_seen = sees.get(Point(x, y), '.')
            print(points_seen, end='')
        print()


def part1():
    sees = {}
    for p in grid:
        sees[p] = len(can_see(p, grid.copy()))
    pprint(sees)
    ans = (None, 0)
    for p, v in sees.items():
        if v > ans[1]:
            ans = (p, v)

    # part1 point 28, 29, ans 340
    print('part1:', ans)


def asteroids_by_angle(origin, points):
    points.remove(origin)
    angles = {}
    for point in points:
        angle = origin.angle(point)
        existing = angles.get(angle, None)
        if existing is None:
            angles[angle] = [(point, origin.distance(point))]
        else:
            existing.append((point, origin.distance(point)))
    for angle_list in angles.values():
        angle_list.sort(key=lambda x: x[1])
    return angles


def part2(origin):
    roids = asteroids_by_angle(origin, grid.copy())
    rotation = [sorted(iter(roids.keys()))][0]
    ptr = 0
    while rotation[ptr] != -90 and ptr < len(rotation):
        ptr += 1
    print('starting at ptr', rotation[ptr])
    ct = 1
    while len(roids.keys()) > 0:
        print('ptr', rotation[ptr], 'rotation length', len(roids.keys()))
        roid_list = roids.get(rotation[ptr], None)
        if roid_list is None:
            print(f'no roid list found for angle {rotation[ptr]}')
        else:
            asteroid = roid_list.pop(0)
            print(f'shooting asteroid {asteroid} at angle {rotation[ptr]} with shot {ct}!')
            if ct == 200:
                ast = asteroid[0]
                print(f'part 2: {ast.x * 100 + ast.y}')
                exit(0)
            ct += 1
            if len(roid_list) == 0:
                print(f'all asteroids at angle {rotation[ptr]} have been lazered!')
                del roids[rotation[ptr]]
        ptr += 1
        if ptr >= len(rotation):
            print(f'reached the end of the rotation. cycling...')
            ptr = 0


# inp = util.get_input(False, '10')
inp = util.get_input(True, '10')
grid, maxx, maxy = parse(inp)
# print(maxx, maxy, grid)
# part1()

# dis is for testing...
# o = Point(11, 13)
# dis is for real...
o = Point(28, 29)
part2(o)
