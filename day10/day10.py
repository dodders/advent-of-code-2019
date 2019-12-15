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
    # with_angles = [(origin, get_angle(origin, point)) for point in points]
    for point in points:
        angle = origin.angle(point)
        existing = angles.get(angle, None)
        if existing is None:
            angles[angle] = (origin, point, origin.distance(point))
            # print(f'angle from {origin} to {point} is {angle} is new')
        else:
            if origin.distance(point) < existing[2]:
                # print(f'angle from {origin} to {point} is {angle} replacing {existing}')
                angles[angle] = (origin, point, origin.distance(point))
    # print(angles)
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


inp = util.get_input(False, '10')
grid, maxx, maxy = parse(inp)
print(maxx, maxy, grid)
part1()