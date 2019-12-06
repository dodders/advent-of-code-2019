import util

# inp = util.get_input(False, '05')
inp = util.get_input(True, '05')
stack = [int(i) for i in inp[0].split(',')]
ptr = 0
sizes = {1: 4, 2: 4, 3: 2, 4: 2}


def put_addr(addr, value):
    stack[addr] = value


def get_addr(mode, addr):
    if mode == '1':
        return addr
    else:
        return stack[addr]


class Opcode:
    op, m1, m2, m3, p1, p2, p3 = None, None, None, None, None, None, None

    def __repr__(self):
        return "op: %s modes :%s %s %s params: %s %s %s" % (self.op, self.m1, self.m2, self.m3, self.p1, self.p2, self.p3)

    def __init__(self, s):
        self.op = int(s[-2:])
        if self.op == 99:
            print('99! halting.')
            exit(0)
        self.m1 = s[-3:-2]
        self.m2 = s[-4:-3]
        self.m3 = s[-5:-4]
        self.p1 = stack[ptr + 1]
        self.p2 = stack[ptr + 2]
        self.p3 = stack[ptr + 3]

    def run(self):
        if self.op == 1:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            res = v1 + v2
            put_addr(self.p3, res)
            return 4

        elif self.op == 2:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            put_addr(self.p3, v1 * v2)
            return 4

        elif self.op == 3:
            # i = input('-->')
            i = 1
            put_addr(self.p1, i)
            return 2

        elif self.op == 4:
            print('op 4:', get_addr(0, self.p1))
            # print('op 4:', self.p1)
            return 2

        else:
            print('invalid opcode:', self.op)
            exit(1)


# part1 5346030
while True:
    op = Opcode(str(stack[ptr]))
    ptr = ptr + op.run()
    print(ptr, ':', stack)
