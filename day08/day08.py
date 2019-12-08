import util

def count_char(s, c):
    return len([x for x in s if x == c])


def get_layers(raw, width, height):
    ret = []
    layer_size = width * height
    for i in range(0, len(raw), layer_size):
        ret.append(raw[i:i + layer_size])
    return ret


def part1():
    counts = [(l, count_char(l, '0'), count_char(l, '1'), count_char(l, '2')) for l in layers]
    print(counts)
    least_zeros = min(counts, key=lambda x: x[1])
    print(least_zeros)
    # part1 2975
    print('part 1 is %d' % (int(least_zeros[2]) * int(least_zeros[3])))


def get_color(position, layers):
    # 0 is black, 1 is white, and 2 is transparent.
    for layer in layers:
        color = layer[position]
        if color is not '2':
            return color
    return color


def pprint(image, width, height):
    for y in range(0, height):
        for x in range(0, width):
            pixel = image[x + y * width]
            if pixel == '1':
                print('X', end='')
            else:
                print(' ', end='')
        print()


def part2(layers, width, height):
    image = []
    size = width * height
    for x in range(0, size):
        image.append(get_color(x, layers))
    print(image)
    pprint(image, width, height)



# layers = get_layers(inp, 25 * 6)
# part1()

# inp = util.get_input(False, '08')[0]
# width = 2
# height = 2
inp = util.get_input(True, '08')[0]
print(inp)
width = 25
height = 6
layers = get_layers(inp, width, height)

# part2 EHRUE
part2(layers, width, height)



