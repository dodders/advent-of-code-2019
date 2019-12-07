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


def print_stack():
    ts = list((enumerate(stack)))
    print('ptr:', ptr, ' ', end='')
    for t in ts:
        print("%d:%d, " % (t[0], t[1]), sep=' ', end='')
    print()


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

    def run(self):
        if self.op == 1:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            self.p3 = stack[ptr + 3]
            res = v1 + v2
            put_addr(self.p3, res)
            return ptr + 4
        elif self.op == 2:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            self.p3 = stack[ptr + 3]
            put_addr(self.p3, v1 * v2)
            return ptr + 4
        elif self.op == 3:
            i = input('-->').strip()
            # i = 8
            put_addr(self.p1, int(i))
            return ptr + 2
        elif self.op == 4:
            print('op 4:', get_addr(self.m1, self.p1))
            return ptr + 2
        # jump if true
        elif self.op == 5:
            v1 = get_addr(self.m1, self.p1)
            if v1 > 0:
                return get_addr(self.m2, self.p2)
            else:
                return ptr + 3
        # jump if false
        elif self.op == 6:
            v1 = get_addr(self.m1, self.p1)
            if v1 == 0:
                return get_addr(self.m2, self.p2)
            else:
                return ptr + 3
        # less than
        elif self.op == 7:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            self.p3 = stack[ptr + 3]
            if v1 < v2:
                put_addr(self.p3, 1)
            else:
                put_addr(self.p3, 0)
            return ptr + 4
        # equals
        elif self.op == 8:
            v1 = get_addr(self.m1, self.p1)
            v2 = get_addr(self.m2, self.p2)
            self.p3 = stack[ptr + 3]
            if v1 == v2:
                put_addr(self.p3, 1)
            else:
                put_addr(self.p3, 0)
            return ptr + 4
        else:
            print('invalid opcode:', self.op)
            exit(1)


# part1 5346030
while True:
    print_stack()
    op = Opcode(str(stack[ptr]))
    print(op)
    ptr = op.run()
