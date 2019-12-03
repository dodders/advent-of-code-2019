import util

inp = util.get_input(False, '03')
path1 = inp[0].split(',')
path2 = inp[1].split(',')
print(path1, path2)

grid = {}


def put(point):
    if point in grid.keys():
        grid[point] += 1
    else:
        grid[point] = 1


def do_path(start, path):
    #


start = (0, 0)
do_path(start, path1)
do_path(start, path2)

