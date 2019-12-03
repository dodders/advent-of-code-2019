import util

# inp = util.get_input(False, '02')
inp = util.get_input(True, '02')
original_stack = [int(i) for i in inp[0].split(',')]
print(original_stack)


def part1(a, b):
    stack = original_stack.copy()
    stack[1] = a
    stack[2] = b
    ptr = 0
    while True:
        if stack[ptr] == 1:
            stack[stack[ptr + 3]] = stack[stack[ptr + 1]] + stack[stack[ptr + 2]]
        elif stack[ptr] == 2:
            stack[stack[ptr + 3]] = stack[stack[ptr + 1]] * stack[stack[ptr + 2]]
        elif stack[ptr] == 99:
            print('finishing stack:', stack)
            print('part 1 position zero:', stack[0])
            return stack[0]
        else:
            print('Stack error:', stack, ptr)
            exit(1)
        ptr = ptr + 4


# part 1 5866663
p1 = part1(12, 2)
print('part1:', p1)

# part2 x=42, y=59, answer=4259
for x in range(0, 100):
    for y in range(0, 100):
        ans = part1(x, y)
        print('x', x, 'y', y, 'ans', ans)
        if ans == 19690720:
            print('part2 x', x, 'y', y, 'answer:', 100 * x + y)
            exit(0)

print('no answer found.')


